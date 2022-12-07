import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Day07 {

    public static Directory rootDirectory = new Directory("/");
    public static String[] commands;

    static {
        try {
            commands = new Scanner(new java.io.File("2022\\Day07\\data.txt")).useDelimiter("\\Z").next().split("\r\n");
            commands = Arrays.copyOfRange(commands, 1, commands.length);
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }

        Directory currentDirectory = rootDirectory;
        for (String command : commands) {
            String[] args = command.split(" ");
            if (args[0].equals("$")) {
                if (args[1].equals("cd")) {
                    if (args[2].equals("..")) {
                        currentDirectory = currentDirectory.containerDirectory;
                    } else {
                        currentDirectory = currentDirectory.getDirectory(args[2]);
                    }
                }
            } else {
                if (args[0].equals("dir")) {
                    if (!currentDirectory.hasDirectory(args[1])) {
                        currentDirectory.addDirectory(new Directory(args[1], currentDirectory));
                    }
                } else {
                    if (!currentDirectory.hasFile(args[1])) {
                        currentDirectory.addFile(new File(Long.parseLong(args[0]), args[1]));
                    }
                }
            }
        }
    }

    public static long part1() {
        return getSumOfDirectoriesBelow(100000, rootDirectory);
    }

    public static long part2() {
        long spaceNeeded = 30000000 - (70000000 - rootDirectory.getTotalSize());
        return getSizeOfSmallestBelow(spaceNeeded, rootDirectory, rootDirectory.getTotalSize());
    }

    public static long getSumOfDirectoriesBelow(long maxSize, Directory directory) {
        long count = directory.getTotalSize() <= maxSize ? directory.getTotalSize() : 0;
        for (Directory subDirectory : directory.directories) {
            count += getSumOfDirectoriesBelow(maxSize, subDirectory);
        }
        return count;
    }

    public static long getSizeOfSmallestBelow(long minSize, Directory directory, long smallest) {
        if (directory.getTotalSize() >= minSize) {
            smallest = Math.min(directory.getTotalSize(), smallest);
        } else {
            return smallest;
        }
        for (Directory subDirectory : directory.directories) {
            smallest = Math.min(smallest, getSizeOfSmallestBelow(minSize, subDirectory, smallest));
        }
        return smallest;
    }

    public static void main(String[] args) {
        System.out.println(part1());
        System.out.println(part2());
    }

    public static class Directory {
        private final ArrayList<Directory> directories = new ArrayList<>();
        private final ArrayList<File> files = new ArrayList<>();
        private Directory containerDirectory;
        private final String name;

        public Directory(String name) {
            this.name = name;
        }

        public Directory(String name, Directory containerDirectory) {
            this(name);
            this.containerDirectory = containerDirectory;
        }

        public void addDirectory(Directory directory) {
            directories.add(directory);
        }

        public void addFile(File file) {
            files.add(file);
        }

        public long getTotalSize() {
            return directories.stream()
                              .map(Directory::getTotalSize)
                              .mapToLong(Long::longValue)
                              .sum() + files.stream()
                                            .map(File::getSize)
                                            .mapToLong(Long::longValue)
                                            .sum();
        }

        public Directory getDirectory(String name) {
            return directories.stream()
                              .filter(directory -> directory.name.equals(name))
                              .findFirst()
                              .orElseThrow(() -> new RuntimeException("Could not find directory"));
        }

        public boolean hasDirectory(String name) {
            return directories.stream()
                              .anyMatch(directory -> directory.name.equals(name));
        }

        public boolean hasFile(String name) {
            return files.stream()
                        .anyMatch(file -> file.name.equals(name));
        }
    }

    public static class File {
        private final long size;
        private final String name;

        public File(long size, String name) {
            this.size = size;
            this.name = name;
        }

        public long getSize() {
            return size;
        }
    }
}
package agh.ics.oop;

import java.util.ArrayList;

public class World {
    public static void main(String[] args) {
        System.out.println("System Start");

        ArrayList<Direction> directions = new ArrayList<>();
        for(String arg : args) {
            switch (arg) {
                case "f":
                    directions.add(Direction.FORWARD);
                    break;
                case "b":
                    directions.add(Direction.BACKWARD);
                    break;
                case "r":
                    directions.add(Direction.RIGHT);
                    break;
                case "l":
                    directions.add(Direction.LEFT);
                    break;
            };
        }

        run(directions);

        System.out.println("System Finish");
    }

    private static void run(ArrayList<Direction> directions) {
        for(Direction dir : directions) {
            System.out.print(switch (dir) {
                case FORWARD -> "The pet is walking forward\n";
                case BACKWARD -> "The pet is walking back\n";
                case RIGHT -> "The pet is walking right\n";
                case LEFT -> "The pet is walking left\n";
            });
        }
    }
}

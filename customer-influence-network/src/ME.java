class ME extends Thread {
    static boolean lock = false;
    int id;

    ME(int id) { this.id = id; }

    public void run() {
        while (lock);
        lock = true;

        System.out.println("Process " + id + " in CS");

        try { Thread.sleep(500); } catch (Exception e) {}

        lock = false;
    }

    public static void main(String[] args) {
        new ME(1).start();
        new ME(2).start();
    }
}
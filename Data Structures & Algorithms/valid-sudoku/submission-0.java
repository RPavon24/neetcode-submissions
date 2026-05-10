
class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Use hash sets to track seen numbers in rows, columns, and sub-boxes
        HashSet<String> seen = new HashSet<>();

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char current = board[i][j];
                if (current != '.') {
                    // Create identifiers for rows, columns, and boxes
                    String rowCheck = current + " in row " + i;
                    String colCheck = current + " in column " + j;
                    String boxCheck = current + " in box " + (i / 3) + "-" + (j / 3);

                    // Check if any identifier is already seen
                    if (!seen.add(rowCheck) || !seen.add(colCheck) || !seen.add(boxCheck)) {
                        return false;
                    }
                }
            }
        }
        return true;
    }
}

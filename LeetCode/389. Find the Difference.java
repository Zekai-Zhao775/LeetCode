class Solution {
    public char findTheDifference(String s, String t) {
        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();
        int sum = 0;
        for (char c : tArr) {
            sum += c;
        }
        for (char c: sArr) {
            sum -= c;
        }
        return (char) sum;
    }
}
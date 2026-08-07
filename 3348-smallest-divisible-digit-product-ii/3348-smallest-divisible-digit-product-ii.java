import java.util.*;

class Solution {
    public String smallestNumber(String num, long t) {
        // Step 1: Extract prime factors of t (must only contain 2, 3, 5, 7)
        long temp = t;
        int[] tFactors = new int[8]; // indices 2, 3, 5, 7
        int[] primes = {2, 3, 5, 7};
        for (int p : primes) {
            while (temp % p == 0) {
                tFactors[p]++;
                temp /= p;
            }
        }
        if (temp > 1) return "-1"; // Prime factor > 7 exists

        int n = num.length();

        // Step 2: Check if num itself is zero-free and already satisfies t
        if (!num.contains("0")) {
            int[] currentFactors = new int[8];
            for (char c : num.toCharArray()) {
                addFactors(currentFactors, c - '0', 1);
            }
            if (isSatisfied(tFactors, currentFactors)) {
                return num;
            }
        }

        // Step 3: Try maintaining prefix num[0...i-1] and replacing num[i] with a larger digit
        int firstZero = num.indexOf('0');
        int maxPrefix = (firstZero != -1) ? firstZero : n - 1;

        int[] prefixFactors = new int[8];
        for (int i = 0; i < maxPrefix; i++) {
            addFactors(prefixFactors, num.charAt(i) - '0', 1);
        }

        for (int i = maxPrefix; i >= 0; i--) {
            int startDigit = num.charAt(i) - '0';
            int remLen = n - 1 - i;

            for (int d = startDigit + 1; d <= 9; d++) {
                int[] reqFactors = getRemainingFactors(tFactors, prefixFactors);
                addFactors(reqFactors, d, -1);

                if (canSatisfy(reqFactors, remLen)) {
                    StringBuilder sb = new StringBuilder();
                    sb.append(num.substring(0, i)).append(d);
                    sb.append(buildSmallestSuffix(reqFactors, remLen));
                    return sb.toString();
                }
            }

            // Backtrack prefix factors for the previous position
            if (i > 0) {
                addFactors(prefixFactors, num.charAt(i - 1) - '0', -1);
            }
        }

        // Step 4: If no same-length solution works, extend length to n + 1 (or more)
        int targetLen = n + 1;
        while (!canSatisfy(tFactors, targetLen)) {
            targetLen++;
        }
        return buildSmallestSuffix(tFactors, targetLen);
    }

    // Adds/subtracts prime factors of digit d
    private void addFactors(int[] factors, int d, int sign) {
        if (d == 2) factors[2] += sign;
        else if (d == 3) factors[3] += sign;
        else if (d == 4) factors[2] += 2 * sign;
        else if (d == 5) factors[5] += sign;
        else if (d == 6) { factors[2] += sign; factors[3] += sign; }
        else if (d == 7) factors[7] += sign;
        else if (d == 8) factors[2] += 3 * sign;
        else if (d == 9) factors[3] += 2 * sign;
    }

    private int[] getRemainingFactors(int[] tFactors, int[] usedFactors) {
        int[] req = new int[8];
        for (int p : new int[]{2, 3, 5, 7}) {
            req[p] = Math.max(0, tFactors[p] - usedFactors[p]);
        }
        return req;
    }

    private boolean isSatisfied(int[] req, int[] current) {
        for (int p : new int[]{2, 3, 5, 7}) {
            if (current[p] < req[p]) return false;
        }
        return true;
    }

    // Checks if factors can be accommodated in `length` digits
    private boolean canSatisfy(int[] factors, int length) {
        int c2 = Math.max(0, factors[2]);
        int c3 = Math.max(0, factors[3]);
        int c5 = Math.max(0, factors[5]);
        int c7 = Math.max(0, factors[7]);

        int slotsNeeded = c7 + c5;
        // Pack 2s and 3s efficiently into 8, 9, 6, 4, 3, 2
        int count8 = c2 / 3;
        c2 %= 3;
        int count9 = c3 / 2;
        c3 %= 2;

        slotsNeeded += count8 + count9;
        if (c2 == 2 && c3 == 1) slotsNeeded += 2;      // e.g., 8 and 9 or 4 and 6
        else if (c2 == 2) slotsNeeded += 1;            // 4
        else if (c2 == 1 && c3 == 1) slotsNeeded += 1; // 6
        else if (c2 == 1 || c3 == 1) slotsNeeded += 1; // 2 or 3

        return slotsNeeded <= length;
    }

    // Greedily constructs the lexicographically smallest valid suffix
    private String buildSmallestSuffix(int[] reqFactors, int length) {
        StringBuilder sb = new StringBuilder();
        int[] currReq = reqFactors.clone();

        for (int pos = 0; pos < length; pos++) {
            int remLen = length - 1 - pos;
            for (int d = 1; d <= 9; d++) {
                int[] nextReq = currReq.clone();
                addFactors(nextReq, d, -1);

                if (canSatisfy(nextReq, remLen)) {
                    sb.append(d);
                    currReq = nextReq;
                    break;
                }
            }
        }
        return sb.toString();
    }
}
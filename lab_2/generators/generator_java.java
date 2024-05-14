import java.security.SecureRandom;

public class SecureRandomBinaryGenerator {
    public static void main(String[] args) {
        String randomBinarySequence = generateRandomBinarySequence();
        System.out.println(randomBinarySequence);
    }

    public static String generateRandomBinarySequence() {
        SecureRandom secureRandom = new SecureRandom();
        byte[] randomBytes = new byte[16]; 
        secureRandom.nextBytes(randomBytes);
        StringBuilder sb = new StringBuilder();
        for (byte b : randomBytes) {
            for (int i = 0; i < 8; i++) {
                sb.append((b >> (7 - i)) & 1);
            }
        }
        return sb.toString();
    }
}
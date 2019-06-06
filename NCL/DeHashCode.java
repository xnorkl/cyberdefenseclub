import java.io.IOException;
import java.io.PrintStream;
import java.security.NoSuchAlgorithmException;

public class DeHashCode
{

    public DeHashCode()
    {
    }

    public static void main(String args[])
        throws IOException, NoSuchAlgorithmException
    {
        if(args.length != 1)
        {
            System.out.println("Usage: java HashCode <tid>");
            System.exit(1);
        }
        byte abyte0[] = args[0].getBytes();
        int i = 0;
        for(int j = 0; j < abyte0.length; j++)
            i += (0xfe ^ abyte0[j]) % 10000;

        String s = (
			new StringBuilder()).append("SKY-JDEC-").append(String.format("%04d", 
			new Object[] {
				Integer.valueOf(i)
			})).toString();
        
	System.out.println((new StringBuilder()).append("The Java hashcode of the flag is: ").append(s.hashCode()).append(". Good luck").toString());
	System.out.println(s);
    }
}

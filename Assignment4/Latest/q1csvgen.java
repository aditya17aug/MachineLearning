import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.Random;

public class q1csvgen {

	public static void main(String[] args) throws IOException {
		genrate();
	}

	private static void genrate() throws IOException {
		StringBuilder title = new StringBuilder();
		for (int i = 1; i <= 10; i++) {
			title.append("attribute").append(i).append(",");
		}
		String strTitle = title.substring(0, title.length() - 1);
		strTitle = strTitle + ",class";
		Files.write(Paths.get("q1.csv"), strTitle.getBytes());
		for (int n = 0; n < 1000; n++) {
			Random random = new Random();
			StringBuilder id = new StringBuilder();
			float classAttr = 0.0f;
			for (int i = 0; i < 10; i++) {
				int randomNum = random.nextInt(10000);
				if (i == 0)
					classAttr = randomNum / 100;
				id.append(String.format("%04d", randomNum)).append(",");
			}
			id.append("x").append(String.valueOf(classAttr));
			System.out.println(id);
			Files.write(Paths.get("q1.csv"), "\n".getBytes(), StandardOpenOption.APPEND);
			Files.write(Paths.get("q1.csv"), id.toString().getBytes(), StandardOpenOption.APPEND);
		}
	}
}

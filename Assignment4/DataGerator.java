import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class DataGerator {

	public static void main(String[] args) throws IOException {
		fileGenerator();
	}

	private static void fileGenerator() throws IOException {
		StringBuilder title = new StringBuilder();
		for (int i = 1; i <= 10; i++) {
			title.append("a").append(i).append(",");
		}
		String strTitle = title.substring(0, title.length() - 1);
		strTitle = strTitle + ",class";
		Files.write(Paths.get("data.csv"), strTitle.getBytes());
		for (int i = 1; i <= 100; i++) {
			int data = 1000*i;
			String dataStr = "";
			for (int j = 0; j < 10; j++) {
				int[] array = new int[10];
				for (int k = 0; k < 10; k++) {
					if (j == k) {
						array[k] = data + 10;
					} else {
						array[k] = data;
					}
				}
				dataStr = IntStream.of(array).mapToObj(Integer::toString).collect(Collectors.joining(","));
				Files.write(Paths.get("data.csv"), "\n".getBytes(), StandardOpenOption.APPEND);
				String classAttr = "";
				for(int k=0; k<i; k++) {
					classAttr = classAttr + "#";
				}
				dataStr = dataStr + "," + String.valueOf(classAttr);
				Files.write(Paths.get("data.csv"), dataStr.getBytes(), StandardOpenOption.APPEND);
			}
		}
	}
}

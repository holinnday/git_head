package chapter13;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Properties;

public class PropertiesEx {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		try {
			Properties pr = new Properties();
			
			FileInputStream reader = new FileInputStream (
					"D:/java/workspace/test/src/chapter13" 
							+ "/config.properties");
			pr.load(reader);
			System.out.println(pr);
			System.out.println("이름 :" + pr.get("name"));
			
			pr.put("subject", "자바");
			System.out.println(pr);
			
			pr.store(new FileOutputStream("D:/java/workspace/test/src/chapter13/" 
							+ "test.properties"), "#save");
		} catch (IOException e) {
			System.out.println(e.getMessage());
		}
	}

}

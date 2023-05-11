package chapter12;

//import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

public class SimpleDateFormatEx2 {
	
	public static void main(String[] args) {
//		SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
//		String strDate = "2020-06-13";
//		
//		Date d = null;
//		try {
//			d = sdf.parse(strDate);
//		} catch (ParseException e) {
//			e.printStackTrace();
//		}
//		System.out.println(d);
//		
//		SimpleDateFormat sf2 = new SimpleDateFormat("yyyy-MM-dd E요일");
//		System.out.println(sf2.format(d));
//		
		
		Calendar cal = Calendar.getInstance();
		cal.set(2020, 5, 13); //월은 +1
		Date day = cal.getTime();
		SimpleDateFormat sdf1, sdf2, sdf3, sdf4;
		sdf1 = new SimpleDateFormat ("yyyy-MM-dd"); 
		sdf2 = new SimpleDateFormat ("yyyy-MM-dd E요일");
		sdf3 = new SimpleDateFormat ("yyyy-MM-dd HH:mm:ss.SSS ");
		sdf4 = new SimpleDateFormat ("yyyy-MM-dd hh:mm:ss a");
		System.out.println(sdf1.format(day));
		System.out.println(sdf2.format(day));
		System.out.println(sdf3.format(day));
		System.out.println(sdf4.format(day));
		
	}
}

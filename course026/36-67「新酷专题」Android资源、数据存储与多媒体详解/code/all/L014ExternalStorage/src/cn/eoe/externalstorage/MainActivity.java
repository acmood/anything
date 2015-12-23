package cn.eoe.externalstorage;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;

import android.app.Activity;
import android.os.Bundle;
import android.os.Environment;
import android.view.Menu;

public class MainActivity extends Activity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		File dir = Environment.getExternalStorageDirectory();
		
		File dataFile = new File(dir, "data.txt");
		//read
		try {
			FileInputStream fis = new FileInputStream(dataFile);
			
			byte[] bytes = new byte[fis.available()];
			fis.read(bytes);
			fis.close();
			
			String str = new String(bytes,"utf-8");
			System.out.println(str);
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		//write
//		try {
//			if (!dataFile.exists()) {
//				dataFile.createNewFile();
//			}
//			
//			FileOutputStream fos = new FileOutputStream(dataFile);
//			fos.write(new String("Hello eoe").getBytes("utf-8"));
//			fos.flush();
//			fos.close();
//			
//		} catch (FileNotFoundException e) {
//			e.printStackTrace();
//		} catch (IOException e) {
//			e.printStackTrace();
//		}
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

}

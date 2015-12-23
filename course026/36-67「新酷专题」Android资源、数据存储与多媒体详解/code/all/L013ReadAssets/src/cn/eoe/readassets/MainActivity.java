package cn.eoe.readassets;

import java.io.IOException;
import java.io.InputStream;

import android.os.Bundle;
import android.app.Activity;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.view.Menu;
import android.widget.ImageView;

public class MainActivity extends Activity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
//		try {
//			InputStream is = getAssets().open("data");
//			
//			byte[] bytes = new byte[is.available()];
//			is.read(bytes);
//			
//			String str = new String(bytes, "utf-8");
//			
//			System.out.println(str);
//		} catch (IOException e) {
//			e.printStackTrace();
//		}
		
		
		ImageView iv = (ImageView) findViewById(R.id.iv);
		
		try {
			InputStream is = getAssets().open("eoe.png");
			
			Bitmap b = BitmapFactory.decodeStream(is);
			iv.setImageBitmap(b);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

}

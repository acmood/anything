package cn.eoe.backbutton;

import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;
import android.widget.Toast;

public class MainActivity extends Activity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}
	
//	private int clickCount = 0;
	
	private long lastClickTime=0;
	
	@Override
	public void onBackPressed() {
//		super.onBackPressed();
//		if (clickCount<1) {
//			Toast.makeText(this, "再按一次后退键退出应用", Toast.LENGTH_SHORT).show();
//			clickCount++;
//		}else{
//			finish();
//		}
		
		if (lastClickTime<=0) {
			Toast.makeText(this, "再按一次后退键退出应用", Toast.LENGTH_SHORT).show();
			lastClickTime = System.currentTimeMillis();
		}else{
			long currentClickTime = System.currentTimeMillis();
			if (currentClickTime-lastClickTime<1000) {
				finish();
			}else{
				Toast.makeText(this, "再按一次后退键退出应用", Toast.LENGTH_SHORT).show();
				lastClickTime = currentClickTime;
			}
		}
	}

}

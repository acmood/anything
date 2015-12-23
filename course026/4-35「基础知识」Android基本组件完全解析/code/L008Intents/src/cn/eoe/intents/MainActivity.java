package cn.eoe.intents;

import java.io.File;

import android.net.Uri;
import android.os.Bundle;
import android.app.Activity;
import android.content.ComponentName;
import android.content.Intent;
import android.view.Menu;
import android.view.View;

public class MainActivity extends Activity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		findViewById(R.id.btnStartAty1).setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				
//				Intent i = new Intent();
//				i.setComponent(new ComponentName("cn.eoe.intents", "cn.eoe.intents.Aty1"));
				
				Intent i = new Intent("cn.eoe.intents.intent.action.Aty1");
				startActivity(i);
			}
		});
		
		
		findViewById(R.id.btnOpenImage).setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				File f = new File("/mnt/sdcard/1.jpg");
				Intent i = new Intent(Intent.ACTION_VIEW);
				i.setDataAndType(Uri.fromFile(f), "image/*");
				startActivity(i);
			}
		});
		
		findViewById(R.id.btnDel10086).setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				
				Intent i = new Intent(Intent.ACTION_VIEW);
				i.setData(Uri.parse("tel:10086"));
				startActivity(i);
				
			}
		});
		
		findViewById(R.id.btnNavToeoe).setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				Intent i = new Intent(Intent.ACTION_VIEW, Uri.parse("http://www.eoe.cn"));
				startActivity(i);
			}
		});
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

}

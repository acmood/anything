package cn.eoe.activitylc;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends Activity {
	
	
	private Button btnStartAty1;
	private TextView tvOut;
	

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		tvOut = (TextView) findViewById(R.id.tvOut);
		btnStartAty1 = (Button) findViewById(R.id.btnStartAty1);
		btnStartAty1.setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				
				Intent i = new Intent(MainActivity.this, Aty1.class);
//				Intent i = new Intent();
//				i.setClassName("cn.eoe.activitylc", "cn.eoe.activitylc.Aty1");
				
//				i.putExtra("txt", "Hello Aty1");
				
				Bundle data = new Bundle();
				data.putString("txt", "Hello Aty1");
				
				i.putExtras(data);
//				startActivity(i);
				
				startActivityForResult(i, 0);
			}
		});
		
		System.out.println("onCreate");
	}
	
	@Override
	protected void onActivityResult(int requestCode, int resultCode, Intent data) {
		
		String result = data.getStringExtra("result");
		tvOut.setText(result);
		
		super.onActivityResult(requestCode, resultCode, data);
	}
	

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}
	
	
	@Override
	protected void onStart() {
		// TODO Auto-generated method stub
		super.onStart();
		
		System.out.println("onStart");
	}
	
	@Override
	protected void onResume() {
		// TODO Auto-generated method stub
		super.onResume();
		
		System.out.println("onResume");
	}
	
	@Override
	protected void onPause() {
		// TODO Auto-generated method stub
		super.onPause();
		
		System.out.println("onPause");
	}
	
	@Override
	protected void onStop() {
		// TODO Auto-generated method stub
		super.onStop();
		
		System.out.println("onStop");
	}
	
	@Override
	protected void onDestroy() {
		// TODO Auto-generated method stub
		super.onDestroy();
		
		System.out.println("onDestory");
	}
	
	@Override
	protected void onRestart() {
		// TODO Auto-generated method stub
		super.onRestart();
		
		System.out.println("onRestart");
	}
}

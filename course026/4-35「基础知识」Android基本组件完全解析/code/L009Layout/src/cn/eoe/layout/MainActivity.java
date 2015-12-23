package cn.eoe.layout;

import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.LinearLayout;

public class MainActivity extends Activity {
	
	private Button btn;
	private LinearLayout mainLayout;
	private OnClickListener btnClickHandler=new OnClickListener() {
		
		@Override
		public void onClick(View v) {
			mainLayout.removeView(v);
		}
	};

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.linear_layout);
		
		mainLayout = (LinearLayout) findViewById(R.id.mainLayout);
		
		for (int i = 0; i < 5; i++) {
			btn = new Button(this);
			btn.setText("Remove me "+i);
//			mainLayout.addView(btn);
			mainLayout.addView(btn, -2, -2);
//			mainLayout.addView(btn, LinearLayout.LayoutParams.WRAP_CONTENT, LinearLayout.LayoutParams.WRAP_CONTENT);
			
			btn.setOnClickListener(btnClickHandler);
		}
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}
}

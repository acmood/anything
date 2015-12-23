package cn.eoe.sharedpreferences;

import android.os.Bundle;
import android.app.Activity;
import android.app.AlertDialog;
import android.content.Context;
import android.content.SharedPreferences;
import android.content.SharedPreferences.Editor;
import android.view.Menu;
import android.widget.CheckBox;
import android.widget.CompoundButton;

public class MainActivity extends Activity {
	
	
	private CheckBox cb;
	private SharedPreferences sp;
	private static final String KEY_SHOW_DIALOG_AT_START = "showDialogAtStart";
	

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		sp = getSharedPreferences("mysp", Context.MODE_PRIVATE);
		
		cb = (CheckBox) findViewById(R.id.cb);
		cb.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
			
			@Override
			public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
				Editor e = sp.edit();
				e.putBoolean(KEY_SHOW_DIALOG_AT_START, isChecked);
				e.commit();
			}
		});
		
		cb.setChecked(sp.getBoolean(KEY_SHOW_DIALOG_AT_START, false));
		
		if (cb.isChecked()) {
			new AlertDialog.Builder(this).setTitle("欢迎").setMessage("你好，欢迎使用我").setPositiveButton("关闭", null).show();
		}
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

}

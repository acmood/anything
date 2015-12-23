package cn.eoe.usinglistview;

import android.app.Activity;
import android.os.Bundle;
import android.widget.ListView;

public class CustomListView extends Activity {

	
	private ListView lv;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.cutom_listview);
		
		lv = (ListView) findViewById(R.id.lv);
		lv.setAdapter(new CustomListViewAdapter(this));
	}
}

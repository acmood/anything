package cn.eoe.usinglistview;

import android.app.ListActivity;
import android.os.Bundle;

public class CustomListViewActivity extends ListActivity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.custom_listview_aty);
		
		setListAdapter(new CustomListViewAdapter(this));
	}
}

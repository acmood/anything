package cn.eoe.usingbaseadapter;

import android.app.ListActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.View;
import android.view.View.OnClickListener;
import android.view.ViewGroup;
import android.widget.TextView;

public class MainActivity extends ListActivity implements OnClickListener {
	
	private MyListAdapter<String> adapter;
	private int index =0 ;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		adapter = new MyListAdapter<String>(this,android.R.layout.simple_list_item_1) {
			
			@Override
			protected void initListCell(int position, View listCell, ViewGroup parent) {
				((TextView)(listCell)).setText(getItem(position));
			}
		};
		
		setListAdapter(adapter);
		
		for (index = 0; index < 5; index++) {
			adapter.add("eoe "+index);
		}
		
		findViewById(R.id.btnAdd).setOnClickListener(this);
		findViewById(R.id.btnRemove).setOnClickListener(this);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

	@Override
	public void onClick(View v) {
		switch (v.getId()) {
		case R.id.btnAdd:
			index++;
			adapter.add("eoe "+index);
			break;
		case R.id.btnRemove:
			adapter.removeLast();
			break;
		default:
			break;
		}
	}

}

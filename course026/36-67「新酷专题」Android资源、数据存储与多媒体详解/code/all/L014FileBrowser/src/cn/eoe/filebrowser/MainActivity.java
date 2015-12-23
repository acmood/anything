package cn.eoe.filebrowser;

import java.io.File;

import android.app.ListActivity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.ListView;

public class MainActivity extends ListActivity {

	
	private ArrayAdapter<EFile> adapter;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		String dir = getIntent().getStringExtra("dir");
		if (dir==null) {
			dir = "/";
		}
		
		File dirFile = new File(dir);
		File[] children = dirFile.listFiles();
		
		adapter = new ArrayAdapter<EFile>(this, android.R.layout.simple_list_item_1);
		
		for (File f : children) {
			adapter.add(new EFile(f));
		}
		
		setListAdapter(adapter);
	}
	
	
	@Override
	protected void onListItemClick(ListView l, View v, int position, long id) {
		
		EFile f = adapter.getItem(position);
		if (f.getFile().isDirectory()) {
			
			Intent i = new Intent(this, MainActivity.class);
			i.putExtra("dir", f.getFile().getAbsolutePath());
			startActivity(i);
		}
		
		super.onListItemClick(l, v, position, id);
	}
	

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

}

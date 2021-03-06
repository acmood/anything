package cn.eoe.camera;

import java.io.File;

import android.app.Activity;
import android.net.Uri;
import android.os.Bundle;
import android.widget.ImageView;

public class ImagePreviewAty extends Activity {

	
	private ImageView iv;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		
		iv = new ImageView(this);
		setContentView(iv);
		
		String path = getIntent().getStringExtra("path");
		if (path!=null) {
			iv.setImageURI(Uri.fromFile(new File(path)));
		}
	}
}

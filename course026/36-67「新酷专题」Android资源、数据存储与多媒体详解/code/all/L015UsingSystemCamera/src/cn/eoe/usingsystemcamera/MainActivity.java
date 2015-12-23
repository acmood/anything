package cn.eoe.usingsystemcamera;

import java.io.File;
import java.io.IOException;

import android.app.Activity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.os.Environment;
import android.provider.MediaStore;
import android.view.Menu;
import android.view.View;
import android.widget.ImageView;

public class MainActivity extends Activity {
	
	
	private static final int REQUEST_CODE_TAKE_PICTURE = 1;
	private ImageView iv;
	
	private File currentImageFile = null;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		iv = (ImageView) findViewById(R.id.iv);
		
		findViewById(R.id.btnStartSystemCamera).setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				
				File dir = new File(Environment.getExternalStorageDirectory(), "pictures");
				if (!dir.exists()) {
					dir.mkdirs();
				}
				currentImageFile = new File(dir, System.currentTimeMillis()+".jpg");
				if (!currentImageFile.exists()) {
					try {
						currentImageFile.createNewFile();
					} catch (IOException e) {
						e.printStackTrace();
					}
				}
				
				Intent i = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
				i.putExtra(MediaStore.EXTRA_OUTPUT, Uri.fromFile(currentImageFile));
				startActivityForResult(i, REQUEST_CODE_TAKE_PICTURE);
			}
		});
	}
	
	
	@Override
	protected void onActivityResult(int requestCode, int resultCode, Intent data) {
		
		switch (requestCode) {
		case REQUEST_CODE_TAKE_PICTURE:
			
			iv.setImageURI(Uri.fromFile(currentImageFile));
			
			break;
		default:
			break;
		}
		
		super.onActivityResult(requestCode, resultCode, data);
	}
	

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

}

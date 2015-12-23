package cn.eoe.playvideo;

import java.io.IOException;

import android.media.MediaPlayer;
import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;
import android.view.SurfaceHolder;
import android.view.SurfaceHolder.Callback;
import android.view.SurfaceView;

public class SurfaceViewPlayerActivity extends Activity {
	
	private SurfaceView sv;
	private SurfaceHolder holder;
	
	private Callback surfaceHolderCallback=new Callback() {
		
		private MediaPlayer mp;
		
		@Override
		public void surfaceDestroyed(SurfaceHolder holder) {
			mp.release();
		}
		
		@Override
		public void surfaceCreated(SurfaceHolder holder) {
			mp = MediaPlayer.create(SurfaceViewPlayerActivity.this, R.raw.movie);
			try {
				mp.prepare();
			} catch (IllegalStateException e) {
				e.printStackTrace();
			} catch (IOException e) {
				e.printStackTrace();
			}
			mp.setDisplay(holder);
			mp.start();
		}
		
		@Override
		public void surfaceChanged(SurfaceHolder holder, int format, int width,
				int height) {
		}
	};

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		
		sv = new SurfaceView(this);
		holder = sv.getHolder();
		holder.addCallback(surfaceHolderCallback);
		
		setContentView(sv);
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

}

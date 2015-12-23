package cn.eoe.playsound;

import java.io.IOException;

import android.media.AudioManager;
import android.media.MediaPlayer;
import android.media.SoundPool;
import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;
import android.view.View;

public class MainActivity extends Activity {
	
	
	private SoundPool sp;
	private int soundId;
	private MediaPlayer mp=null;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		sp = new SoundPool(1, AudioManager.STREAM_MUSIC, 0);
		soundId = sp.load(this, R.raw.note1, 1);
		
		findViewById(R.id.btnPlaySound).setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {				
				sp.play(soundId, 1, 1, 0, 0, 2.0f);
			}
		});
		
		findViewById(R.id.btnPlaySong).setOnClickListener(new View.OnClickListener() {
			
			@Override
			public void onClick(View v) {
				if (mp!=null) {
					mp.start();
				}
			}
		});
	}
	
	@Override
	protected void onResume() {
		
		mp= MediaPlayer.create(this, R.raw.song);
		try {
			mp.prepare();
		} catch (IllegalStateException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		super.onResume();
	}
	
	@Override
	protected void onPause() {
		
		if (mp!=null) {
			mp.release();
		}
		
		super.onPause();
	}
	

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

}

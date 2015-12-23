package cn.eoe.playvideo;

import android.app.Activity;
import android.os.Bundle;
import android.widget.MediaController;
import android.widget.VideoView;

public class VideoViewPlayerAvtivity extends Activity {

	
	private VideoView vv;
	
	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		
		vv =new VideoView(this);
		setContentView(vv);
		vv.setVideoPath("/mnt/sdcard/movie.mp4");
		vv.setMediaController(new MediaController(this));
	}
}

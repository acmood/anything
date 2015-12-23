package cn.eoe.usingbc;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;

public class MyBC extends BroadcastReceiver {

	
	public static final String ACTION = "cn.eoe.usingbc.intent.action.MyBC";
	
	
	@Override
	public void onReceive(Context context, Intent intent) {
		System.out.println("onReceive,data="+intent.getStringExtra("txt"));
	}

}

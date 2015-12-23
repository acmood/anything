package cn.eoe.usinglistview;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

public class CustomListViewAdapter extends BaseAdapter {
	
	
	private Context context=null;
	
	public CustomListViewAdapter(Context context) {
		this.context= context;
	}

	public Context getContext() {
		return context;
	}
	

//	private String[] data = new String[]{"eoe1","eoe2","eoe3","eoe4","eoe5","eoe6","eoe1","eoe7","eoe8","eoe9","eoe10","eoe11","eoe12","eoe13","eoe14","eoe15"};
	
	private CustomListCellData[] data = new CustomListCellData[]{
			new CustomListCellData("img1", "dec img1", R.drawable.img1),
			new CustomListCellData("img2", "dec img2", R.drawable.img2),
			new CustomListCellData("img3", "dec img3", R.drawable.img3),
	};
	
	@Override
	public View getView(int position, View convertView, ViewGroup parent) {
		
//		System.out.println(">>>>>>>>>>>>>");
//		
//		TextView tv=null;
//		
//		if (convertView!=null) {
//			tv =(TextView) convertView;
//		}else{
//			tv = new TextView(CustomListView.this);
//		}
//		
//		tv.setTextSize(50);
//		tv.setText(getItem(position));
//		
//		return tv;
		
		LinearLayout ll = null;
		if (convertView!=null) {
			ll = (LinearLayout) convertView;
		}else{
			ll = (LinearLayout) LayoutInflater.from(getContext()).inflate(R.layout.custom_listcell, null);
		}
		
		CustomListCellData data = getItem(position);
		
		ImageView icon = (ImageView) ll.findViewById(R.id.icon);
		TextView name = (TextView) ll.findViewById(R.id.name);
		TextView dec = (TextView) ll.findViewById(R.id.dec);
		
		icon.setImageResource(data.iconId);
		name.setText(data.name);
		dec.setText(data.dec);
		
		return ll;
	}
	
	@Override
	public long getItemId(int position) {
		return position;
	}
	
	@Override
	public CustomListCellData getItem(int position) {
		return data[position];
	}
	
	@Override
	public int getCount() {
		return data.length;
	}

}

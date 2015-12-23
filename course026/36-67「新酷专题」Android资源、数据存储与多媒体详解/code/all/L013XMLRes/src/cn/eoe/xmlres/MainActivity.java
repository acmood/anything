package cn.eoe.xmlres;

import java.io.IOException;

import org.xmlpull.v1.XmlPullParserException;

import android.os.Bundle;
import android.app.Activity;
import android.content.res.XmlResourceParser;
import android.view.Menu;

public class MainActivity extends Activity {

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		
		XmlResourceParser p = getResources().getXml(R.xml.users);
		
		try {
			while(p.getEventType()!=XmlResourceParser.END_DOCUMENT){
				if (p.getEventType()==XmlResourceParser.START_TAG) {
					
					if (p.getName().equals("user")) {
						String name = p.getAttributeValue(null, "name");
						String age = p.getAttributeValue(null,"age");
						
						System.out.println(String.format("名字：%s,年龄：%s", name,age));
					}
				}
				
				p.next();
			}
		} catch (XmlPullParserException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.main, menu);
		return true;
	}

}

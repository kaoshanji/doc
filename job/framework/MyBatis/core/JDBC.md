``` Java
package top.kaoshanji.xupeng;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.sql.rowset.CachedRowSet;
import javax.sql.rowset.RowSetFactory;
import javax.sql.rowset.RowSetProvider;

/**
 * 演示 JDBC 步骤..
 * @author kaoshanji
 * @date 2017年10月31日上午11:46:31
 */
public class MySqlData {
	
	/**
	 * 获取列表数据...
	 * map : key=field value=value
	 * 数据库里一行数据是 List一个元素,是map集合
	 * list的长度由数据行决定,map的长度由一行字段数量决定
	 * @return
	 */
	public List<Map<String,String>> getColumnValue() {
		List<Map<String,String>> maps = null;
		// 数据库连接相关
		String mysqlUrl 		= "jdbc:mysql://localhost:3306/xx-theme?useUnicode=true&characterEncoding=utf8"
				+ "&autoReconnect=true&zeroDateTimeBehavior=convertToNull";
		String mysqlUsername 	= "root";
		String mysqlPassword 	= "123456";
		String mysqlDriver 		= "com.mysql.jdbc.Driver";
		String sql 				= "SELECT driver_id,account_name,password FROM t_driver_user ";
		String[] columns		= {"driver_id","account_name","password"};
		Connection conn 		= null;
		try {
			// 注册驱动器
			Class.forName(mysqlDriver);
			// 获得数据库连接
			conn = DriverManager.getConnection(mysqlUrl, mysqlUsername, mysqlPassword);
			
			//执行查询
			Statement star = conn.createStatement();
			ResultSet rs = star.executeQuery(sql);
			RowSetFactory factory = RowSetProvider.newFactory();
			CachedRowSet rowSet = factory.createCachedRowSet();
			rowSet.populate(rs);
			
			maps = new ArrayList<>();
			
			// 数据库数据..
			Map<String,String> map = null;
			// 便利一行数据..
            while(rowSet.next()) {
                map = new HashMap<>(columns.length);
                // 一行的每个字段
                for (String s : columns) {
                    map.put(s, String.valueOf(rowSet.getObject(s)));
                }
                maps.add(map);
            }
		} catch (ClassNotFoundException | SQLException e) {
			System.out.println(".........");
			e.printStackTrace();
		} finally {
			try {
				conn.close();
			} catch (SQLException e) {
				System.out.println("------释放数据库连接出错...");
				e.printStackTrace();
			}
		}
		return maps;
	}
	
	public static void main(String args[]) {
		MySqlData sql = new MySqlData();
		List<Map<String,String>> maps = sql.getColumnValue();
		System.out.println(maps);
		
	}
}

```

--------
### 执行结果...

``` JSON
[
    {
        driver_id=1,
        password=132,
        account_name=wuzu1
    },
    {
        driver_id=2,
        password=132,
        account_name=wuzu2
    },
    {
        driver_id=11,
        password=pppp1,
        account_name=xxxx1
    },
    {
        driver_id=12,
        password=pppp2,
        account_name=xxxx2
    },
    {
        driver_id=13,
        password=wuzu,
        account_name=wuzu3
    },
    {
        driver_id=14,
        password=wuzu,
        account_name=wuzu
    },
    {
        driver_id=15,
        password=wuzu,
        account_name=wuzu123
    }
]
```
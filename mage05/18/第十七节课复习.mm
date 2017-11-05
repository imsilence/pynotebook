<map version="1.0.1">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node CREATED="1501292114289" ID="ID_1310202330" MODIFIED="1501292191830" TEXT="&#x7b2c;&#x5341;&#x4e03;&#x8282;&#x8bfe;&#x590d;&#x4e60;">
<node CREATED="1501292202498" ID="ID_1667660161" MODIFIED="1501292468762" POSITION="right" TEXT="&#x4e8b;&#x52a1;">
<node CREATED="1501292207990" ID="ID_1369483535" MODIFIED="1501292223539" TEXT="&#x4e00;&#x7cfb;&#x5217;&#x7684;&#x6570;&#x636e;&#x5e93;&#x64cd;&#x4f5c;&#x540c;&#x65f6;&#x6210;&#x529f;&#x6216;&#x8005;&#x5931;&#x8d25;"/>
<node CREATED="1501292451015" ID="ID_1716675690" MODIFIED="1501292453132" TEXT="&#x6570;&#x636e;&#x5e93;">
<node CREATED="1501292471270" ID="ID_294457586" MODIFIED="1501292473060" TEXT="&#x652f;&#x6301;"/>
<node CREATED="1501292477574" ID="ID_1765299913" MODIFIED="1501292484040" TEXT="mysql engine">
<node CREATED="1501292573028" ID="ID_29714061" MODIFIED="1501292573649" TEXT="InnoDB"/>
</node>
</node>
<node CREATED="1501292256014" ID="ID_1582117148" MODIFIED="1501292257704" TEXT="with"/>
<node CREATED="1501292260636" ID="ID_704371098" MODIFIED="1501292273353" TEXT="form django.db import transaction"/>
<node CREATED="1501292274122" ID="ID_1847188701" MODIFIED="1501292283304" TEXT="with transaction.atomic():">
<node CREATED="1501292312991" ID="ID_351499478" MODIFIED="1501292319042" TEXT="&#x65e0;&#x5f02;&#x5e38;&#x63d0;&#x4ea4;">
<node CREATED="1501292397345" ID="ID_119052333" MODIFIED="1501292401809" TEXT="conn.commit()"/>
</node>
<node CREATED="1501292319292" ID="ID_1083999449" MODIFIED="1501292323927" TEXT="&#x6709;&#x5f02;&#x5e38;&#x56de;&#x6eda;">
<node CREATED="1501292403003" ID="ID_804294217" MODIFIED="1501292408669" TEXT="conn.rollback()"/>
</node>
</node>
</node>
<node CREATED="1501292598048" ID="ID_201218140" MODIFIED="1501292615538" POSITION="right" TEXT="&#x7528;&#x6237;&#x767b;&#x5f55;&#x3001;&#x767b;&#x51fa;">
<node CREATED="1501292643188" ID="ID_317287133" MODIFIED="1501292654582" TEXT="django.contrib.auth"/>
<node CREATED="1501292666004" ID="ID_426672771" MODIFIED="1501292670355" TEXT="&#x7528;&#x6237;&#x8ba4;&#x8bc1;&#x63a5;&#x53e3;">
<node CREATED="1501292698400" ID="ID_1042310434" MODIFIED="1501292711835" TEXT="user = authenticate(username, password)"/>
<node CREATED="1501292751104" ID="ID_1634708458" MODIFIED="1501292755143" TEXT="User"/>
</node>
<node CREATED="1501292774723" ID="ID_1595811778" MODIFIED="1501292781168" TEXT="&#x81ea;&#x5b9a;&#x4e49;&#x7684;&#x529f;&#x80fd;">
<node CREATED="1501292813594" ID="ID_20326108" MODIFIED="1501292815959" TEXT="&#x65b9;&#x6cd5;">
<node CREATED="1501292816694" ID="ID_1771040125" MODIFIED="1501292817106" TEXT="1">
<node CREATED="1501292817968" ID="ID_1403253182" MODIFIED="1501292821848" TEXT="&#x6269;&#x5c55;User&#x8868;">
<node CREATED="1501292885334" ID="ID_1454265108" MODIFIED="1501292895972" TEXT="user.userext.status"/>
</node>
</node>
<node CREATED="1501292831772" ID="ID_147397589" MODIFIED="1501292832298" TEXT="2">
<node CREATED="1501292833316" ID="ID_364749128" MODIFIED="1501292834889" TEXT="&#x81ea;&#x5df1;&#x5199;">
<node CREATED="1501292919992" ID="ID_727149434" MODIFIED="1501292929412" TEXT="&#x5b8c;&#x5168;&#x4e0d;&#x8c03;&#x7528;authenticate">
<node CREATED="1501292958673" ID="ID_824062758" MODIFIED="1501292960637" TEXT="form"/>
</node>
<node CREATED="1501292964230" ID="ID_23520777" MODIFIED="1501292987169" TEXT="backends"/>
</node>
</node>
</node>
</node>
<node CREATED="1501293290940" ID="ID_404349394" MODIFIED="1501293296049" TEXT="&#x7528;&#x6237;&#x72b6;&#x6001;&#x5b58;&#x50a8;">
<node CREATED="1501293297097" ID="ID_893319959" MODIFIED="1501293301252" TEXT="login(request, user)"/>
</node>
<node CREATED="1501293356183" ID="ID_1391047241" MODIFIED="1501293363565" TEXT="&#x68c0;&#x67e5;&#x7528;&#x6237;&#x662f;&#x5426;&#x767b;&#x9646;">
<node CREATED="1501293424248" ID="ID_1212103876" MODIFIED="1501293433035" TEXT="request.user.is_authenticated()"/>
<node CREATED="1501293445388" ID="ID_616010932" MODIFIED="1501293447051" TEXT="request.user">
<node CREATED="1501293447939" ID="ID_1418646452" MODIFIED="1501293451544" TEXT="&#x600e;&#x4e48;&#x6765;&#x7684;"/>
<node CREATED="1501293479931" ID="ID_1085811409" MODIFIED="1501293502617" TEXT="Middleware"/>
</node>
</node>
<node CREATED="1501293547561" ID="ID_693602523" MODIFIED="1501293577250" TEXT="&#x767b;&#x51fa;">
<node CREATED="1501293582799" ID="ID_1849204090" MODIFIED="1501293586838" TEXT="logout(request)"/>
</node>
</node>
<node CREATED="1501292615816" ID="ID_1211242693" MODIFIED="1501292618276" POSITION="right" TEXT="&#x5bc6;&#x7801;&#x91cd;&#x7f6e;">
<node CREATED="1501293632785" ID="ID_281859339" MODIFIED="1501293905486" TEXT="&#x53d1;&#x9001;&#x90ae;&#x4ef6;&#x8fdb;&#x884c;&#x91cd;&#x7f6e;">
<node CREATED="1501293669416" ID="ID_402885167" MODIFIED="1501293681140" TEXT="a">
<node CREATED="1501293682103" ID="ID_906462011" MODIFIED="1501293693923" TEXT="&#x8ba9;&#x7528;&#x6237;&#x544a;&#x8bc9;&#x4f60;&#x53d1;&#x9001;&#x90ae;&#x4ef6;&#x5230;&#x54ea;&#x91cc;"/>
</node>
<node CREATED="1501293711521" ID="ID_642934871" MODIFIED="1501293759310" TEXT="b">
<node CREATED="1501293759289" ID="ID_566589600" MODIFIED="1501293773698" TEXT="&#x70b9;&#x51fb;&#x90ae;&#x4ef6;&#x94fe;&#x63a5;&#x56de;&#x5230;&#x7f51;&#x7ad9;">
<node CREATED="1501293718677" ID="ID_1672913858" MODIFIED="1501293728063" TEXT="validkey + username"/>
</node>
</node>
<node CREATED="1501293754499" ID="ID_995490135" MODIFIED="1501293755963" TEXT="c">
<node CREATED="1501293778023" ID="ID_1933936356" MODIFIED="1501293783808" TEXT="&#x65b0;&#x5bc6;&#x7801;&#x586b;&#x5199;">
<node CREATED="1501293828960" ID="ID_1821714101" MODIFIED="1501293836455" TEXT="password+validkey+username"/>
<node CREATED="1501293807708" ID="ID_1202011464" MODIFIED="1501293819114" TEXT="&#x9a8c;&#x8bc1;&#x662f;&#x5426;&#x6709;&#x4fee;&#x6539;&#x5bc6;&#x7801;&#x7684;&#x610f;&#x56fe;"/>
</node>
</node>
</node>
<node CREATED="1501293899446" ID="ID_1527174110" MODIFIED="1501293902582" TEXT="validkey">
<node CREATED="1501293907229" ID="ID_946896394" MODIFIED="1501293915181" TEXT="&#x6709;&#x6548;&#x65f6;&#x95f4;"/>
</node>
</node>
<node CREATED="1501293982439" ID="ID_1882070552" MODIFIED="1501293991972" POSITION="right" TEXT="views.py">
<node CREATED="1501293992749" ID="ID_312359606" MODIFIED="1501294008729" TEXT="django.views.generic.FormView">
<node CREATED="1501294118466" ID="ID_143148029" MODIFIED="1501294168918" TEXT="&#x5c5e;&#x6027;">
<node CREATED="1501294124583" ID="ID_1825302141" MODIFIED="1501294127040" TEXT="form_class"/>
</node>
<node CREATED="1501294131790" ID="ID_277836974" MODIFIED="1501294134546" TEXT="&#x65b9;&#x6cd5;">
<node CREATED="1501294135297" ID="ID_983865177" MODIFIED="1501294152341" TEXT="form_valid(self, form)"/>
<node CREATED="1501294139015" ID="ID_1260677960" MODIFIED="1501294146256" TEXT="form_invalid(self, form)"/>
</node>
</node>
</node>
</node>
</map>

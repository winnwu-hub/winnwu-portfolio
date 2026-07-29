import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'F:\AI大模型学习\找工作\01 简历\winnwu-portfolio\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Insert 个人简介 after metrics section
new_intro = '''<!-- 个人简介 -->
<section>
  <div class="container">
    <h2 style="margin-bottom:28px;">个人简介</h2>
    <div class="intro-card">
      <div class="intro-main">
        <p>熟悉中日两国社交媒体生态，擅长将日语学习内容转化为适配中国用户的内容产品。对日本流行文化、热点话题有敏锐洞察力，能快速捕捉中日文化差异中的传播爆点。</p>
      </div>
      <div class="intro-tags">
        <span class="skill-tag">中日双语内容</span>
        <span class="skill-tag">跨文化传播</span>
        <span class="skill-tag">日本流行文化洞察</span>
        <span class="skill-tag">用户需求分析</span>
      </div>
    </div>
  </div>
</section>

<!-- 运营平台横排 -->'''

html = html.replace('<!-- 运营平台横排 -->', new_intro)

# 2. Replace 运营思路 section with detailed case study
old_strategy = '''<!-- 运营思路 -->
<section>
  <div class="container">
    <h2 style="margin-bottom:28px;">运营思路</h2>
    <div class="strategy-grid">

      <div class="strategy-item">
        <div class="num">01</div>
        <h3>平台定位与差异化运营</h3>
        <p>根据小红书、视频号、B站各平台的算法机制与用户画像，制定差异化内容策略。同一主题内容按平台特征进行适配改编，而非简单搬运，最大化内容在各平台的自然流量获取效率。</p>
      </div>

      <div class="strategy-item">
        <div class="num">02</div>
        <h3>搜索流量驱动的选题策略</h3>
        <p>以用户搜索意图为核心进行选题与标题关键词布局，结合热点话题与长尾关键词，使内容在发布后持续获得搜索流量，形成稳定的长尾曝光。</p>
      </div>

      <div class="strategy-item">
        <div class="num">03</div>
        <h3>数据驱动的迭代优化</h3>
        <p>每周统计播放量、完播率、互动率、评论反馈等数据，对比不同标题风格、封面设计、发布时间的效果差异，将数据结论直接应用于下一期内容策划，形成"选题 发布 复盘 优化"的闭环。</p>
      </div>

      <div class="strategy-item">
        <div class="num">04</div>
        <h3>内容系列化与用户沉淀</h3>
        <p>围绕核心主题打造系列内容，建立用户对账号的内容预期，提升关注转化和粉丝粘性，实现从单条爆款到账号资产的持续积累。</p>
      </div>

    </div>
  </div>
</section>'''

new_strategy = '''<!-- 核心案例：日语学习账号运营 -->
<section>
  <div class="container">
    <h2 style="margin-bottom:28px;">核心案例：日语学习账号运营</h2>

    <!-- 背景与目标 -->
    <div class="case-block">
      <h3 class="case-subtitle">背景与目标</h3>
      <div class="case-grid-3">
        <div class="case-item">
          <div class="case-icon">🎯</div>
          <h4>目标受众</h4>
          <p>日语零基础/初级学习者、对日本文化感兴趣的人群</p>
        </div>
        <div class="case-item">
          <div class="case-icon">📌</div>
          <h4>账号目标</h4>
          <p>建立垂直领域专业认知，提升粉丝粘性和互动率</p>
        </div>
        <div class="case-item">
          <div class="case-icon">⚠️</div>
          <h4>初期挑战</h4>
          <p>日语学习内容同质化严重，如何做出差异化是核心问题</p>
        </div>
      </div>
    </div>

    <!-- 策略与行动 -->
    <div class="case-block">
      <h3 class="case-subtitle">策略与行动</h3>

      <h4 class="case-section-title">选题策划四大方向</h4>
      <div class="strategy-grid">
        <div class="strategy-item">
          <div class="num">热点型</div>
          <h3>借势IP与热点</h3>
          <p>结合日剧、动漫热点（如《鬼灭之刃》《咒术回战》播出期）做专题内容，借势搜索流量获取初始曝光，同时吸引二次元兴趣用户。</p>
        </div>
        <div class="strategy-item">
          <div class="num">痛点型</div>
          <h3>解决学习痛点</h3>
          <p>针对中国人学日语的常见误区，如"中式日语"、"自动词与他动词混淆"等，用对比方式呈现，通过"共鸣感"驱动互动和收藏。</p>
        </div>
        <div class="strategy-item">
          <div class="num">实用型</div>
          <h3>场景化实用内容</h3>
          <p>围绕旅游、留学、日常购物等高频率场景制作内容，标题精准覆盖搜索关键词，形成长尾流量。代表内容"酒店入住篇"播放量3.8万。</p>
        </div>
        <div class="strategy-item">
          <div class="num">文化型</div>
          <h3>文化差异切入</h3>
          <p>以中日文化差异为切入点，如"读空气"文化、关西腔与标准语差异、日本职场礼仪等，利用好奇心驱动传播和转发。</p>
        </div>
      </div>
    </div>

    <!-- 内容形式与视觉 -->
    <div class="case-block">
      <h3 class="case-subtitle">内容形式与视觉策略</h3>
      <div class="format-grid">
        <div class="format-item">
          <h4>小红书</h4>
          <ul>
            <li>图文笔记：语法卡片 + 场景对话 + 表情包配图</li>
            <li>轮播图：带发音标注，适合收藏场景</li>
            <li>视觉风格：日系柔和色调、手写字体感排版</li>
          </ul>
        </div>
        <div class="format-item">
          <h4>视频号</h4>
          <ul>
            <li>短视频：30-60秒，日语配音 + 中文字幕对照</li>
            <li>混剪内容：日本街头实拍素材 + 教学配音</li>
            <li>封面含关键词标签，统一视觉识别</li>
          </ul>
        </div>
        <div class="format-item">
          <h4>B站</h4>
          <ul>
            <li>中长视频：完整语法讲解 + 场景演绎</li>
            <li>弹幕互动设计，引导评论区和弹幕参与</li>
            <li>标题突出"干货"属性，提升搜索权重</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- 数据复盘与洞察 -->
    <div class="case-block">
      <h3 class="case-subtitle">数据复盘与洞察</h3>
      <div class="insight-grid">
        <div class="insight-card">
          <div class="insight-icon">1</div>
          <p>日语学习类用户对<strong>"中日字幕对照"的视频形式完播率最高</strong>——纯音频/无字幕版本平均完播率低约35%</p>
        </div>
        <div class="insight-card">
          <div class="insight-icon">2</div>
          <p>纯干货语法笔记<strong>收藏率高但互动率低</strong>，后续加入"提问互动"环节（"这句话用日语怎么说？评论区留言"），互动率提升约2倍</p>
        </div>
        <div class="insight-card">
          <div class="insight-icon">3</div>
          <p>标题含<strong>具体场景词</strong>（酒店、便利店、面试）的内容长尾流量占比超60%，远高于泛标题内容</p>
        </div>
        <div class="insight-card">
          <div class="insight-icon">4</div>
          <p>同一主题内容跨平台发布后，<strong>各平台用户关注点不同</strong>：小红书用户偏重收藏实用内容，B站用户更关注互动讨论，视频号用户倾向于转发分享</p>
        </div>
      </div>
    </div>

    <!-- 一句话总结 -->
    <div class="case-summary">
      <p>核心方法论：<strong>选题命中搜索需求 → 内容适配平台特征 → 数据反馈驱动迭代</strong>，形成可持续增长的内容运营闭环。</p>
    </div>

  </div>
</section>'''

html = html.replace(old_strategy, new_strategy)

# 3. Replace 代表内容 section with expanded 代表作品
old_featured = '''<!-- 代表内容 -->
<section>
  <div class="container">
    <h2>代表内容</h2>
    <div class="featured-card">
      <img src="social-media/featured-content.jpg" alt="内容数据详情" loading="lazy" style="width:200px;">
      <div class="featured-info">
        <span class="tag">小红书</span>
        <h4>旅游日语 |【酒店入住篇】</h4>
        <p style="color:#555; font-size:0.9em; margin-top:6px;">
          碎片化日语学习内容，通过场景化教学切入高频需求话题，标题直接命中搜索流量。
        </p>
        <div style="background:#fff; border-left:3px solid #1a1a2e; padding:12px 16px; margin-top:12px; border-radius:0 6px 6px 0; font-size:0.88em; color:#444;">
          <strong>策略分析：</strong>选择"酒店入住"这一高频场景作为切入点，标题精准覆盖搜索关键词；场景化封面配合标题形成搜索吸引力，发布后持续获得自然搜索流量，成为账号长尾曝光的代表内容。
        </div>
        <div class="data-row">
          <div class="item"><div class="num">38,074</div><div class="lbl">播放量</div></div>
          <div class="item"><div class="num">1,683</div><div class="lbl">点赞</div></div>
        </div>
      </div>
    </div>
  </div>
</section>'''

new_featured = '''<!-- 代表作品 -->
<section>
  <div class="container">
    <h2 style="margin-bottom:28px;">代表作品</h2>

    <!-- 实用型 - 有截图 -->
    <div class="featured-card">
      <img src="social-media/featured-content.jpg" alt="旅游日语酒店入住篇" loading="lazy" style="width:200px;">
      <div class="featured-info">
        <span class="tag" style="background:#e74c3c;">实用型</span>
        <span class="tag" style="background:#888; margin-left:6px;">小红书</span>
        <h4>旅游日语 |【酒店入住篇】</h4>
        <p style="color:#555; font-size:0.9em; margin-top:6px;">
          碎片化日语学习内容，通过场景化教学切入高频需求话题，标题直接命中搜索流量。
        </p>
        <div class="data-row">
          <div class="item"><div class="num">38,074</div><div class="lbl">播放量</div></div>
          <div class="item"><div class="num">1,683</div><div class="lbl">点赞</div></div>
        </div>
      </div>
    </div>

    <!-- 更多作品以文本展示 -->
    <div class="works-grid">
      <div class="work-card">
        <span class="tag" style="background:#e74c3c;">痛点型</span>
        <h4>中国人最容易犯的日语错误</h4>
        <p>从常见中式日语切入，用对比方式呈现正确与错误表达，引发"中枪"共鸣，带动评论互动</p>
        <div class="work-data">
          <span>阅读 8,200+</span>
          <span>收藏 600+</span>
        </div>
      </div>
      <div class="work-card">
        <span class="tag" style="background:#9b59b6;">文化型</span>
        <h4>关西腔 vs 标准语</h4>
        <p>以日本地域文化差异为切入点，结合搞笑演绎，利用好奇心驱动跨圈层传播</p>
        <div class="work-data">
          <span>播放 1.2万+</span>
          <span>转发 800+</span>
        </div>
      </div>
      <div class="work-card">
        <span class="tag" style="background:#2ecc71;">实用型</span>
        <h4>N2高频语法合集</h4>
        <p>轮播图形式，排版清晰直接解决备考痛点，收藏型内容，持续获得长尾搜索流量</p>
        <div class="work-data">
          <span>收藏 3,000+</span>
        </div>
      </div>
      <div class="work-card">
        <span class="tag" style="background:#e67e22;">热点型</span>
        <h4>动漫日语 vs 真实日语</h4>
        <p>借势热门动漫IP，用台词对比真实口语表达，反差感强，搜索流量与兴趣推荐双驱动</p>
        <div class="work-data">
          <span>阅读 1.2万+</span>
          <span>收藏 1,000+</span>
        </div>
      </div>
    </div>

  </div>
</section>'''

html = html.replace(old_featured, new_featured)

# 4. Replace 核心能力 section with 技能与工具
old_skills_section = '''<!-- 核心能力 -->
<section>
  <div class="container">
    <h2>核心能力</h2>
    <div class="skills" style="margin-top:16px;">
      <span class="skill-tag">多平台社媒运营</span>
      <span class="skill-tag">内容策划与创作</span>
      <span class="skill-tag">短视频剪辑（Pr/剪映）</span>
      <span class="skill-tag">图文排版</span>
      <span class="skill-tag">Facebook/Instagram 推广</span>
      <span class="skill-tag">KOL 合作</span>
      <span class="skill-tag">运营数据分析</span>
      <span class="skill-tag">AI 工具辅助（ChatGPT/Claude）</span>
      <span class="skill-tag">跨境电商运营</span>
      <span class="skill-tag">独立站搭建</span>
    </div>
  </div>
</section>'''

new_skills_section = '''<!-- 技能与工具 -->
<section>
  <div class="container">
    <h2 style="margin-bottom:28px;">技能与工具</h2>
    <div class="tool-grid">
      <div class="tool-category">
        <h3>内容创作</h3>
        <div class="skills">
          <span class="skill-tag">Canva/醒图（图文排版）</span>
          <span class="skill-tag">剪映/CapCut（视频剪辑）</span>
          <span class="skill-tag">Pr（视频后期）</span>
          <span class="skill-tag">字幕添加与配音</span>
        </div>
      </div>
      <div class="tool-category">
        <h3>数据分析</h3>
        <div class="skills">
          <span class="skill-tag">小红书创作后台</span>
          <span class="skill-tag">视频号数据中心</span>
          <span class="skill-tag">粉丝画像分析</span>
          <span class="skill-tag">完播率/互动率追踪</span>
        </div>
      </div>
      <div class="tool-category">
        <h3>文案与策划</h3>
        <div class="skills">
          <span class="skill-tag">选题规划与关键词策略</span>
          <span class="skill-tag">日语翻译与校对</span>
          <span class="skill-tag">ChatGPT辅助脚本</span>
          <span class="skill-tag">Claude内容优化</span>
        </div>
      </div>
      <div class="tool-category">
        <h3>运营平台</h3>
        <div class="skills">
          <span class="skill-tag">Facebook/Instagram</span>
          <span class="skill-tag">小红书/视频号/B站/抖音</span>
          <span class="skill-tag">微信生态传播</span>
          <span class="skill-tag">海外KOL合作</span>
        </div>
      </div>
    </div>
  </div>
</section>'''

html = html.replace(old_skills_section, new_skills_section)

# 5. Add CSS for new sections
new_css = '''
    /* Intro Card */
    .intro-card {
        background: #f8f9fa;
        border-radius: 12px;
        padding: 28px 32px;
        border: 1px solid #eee;
    }
    .intro-main p {
        font-size: 1em;
        color: #444;
        line-height: 1.8;
    }
    .intro-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 16px;
    }

    /* Case Study */
    .case-block { margin-top: 32px; }
    .case-subtitle {
        font-size: 1.05em;
        color: #1a1a2e;
        margin-bottom: 16px;
        padding-bottom: 6px;
        border-bottom: 2px solid #e8edf5;
    }
    .case-section-title {
        font-size: 0.95em;
        color: #555;
        margin: 20px 0 12px;
    }
    .case-grid-3 {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 16px;
    }
    .case-item {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        border: 1px solid #eee;
    }
    .case-item h4 { font-size: 0.95em; margin: 8px 0 6px; }
    .case-item p { font-size: 0.88em; color: #555; line-height: 1.6; }
    .case-icon { font-size: 1.4em; }

    /* Format Grid */
    .format-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 16px;
    }
    .format-item {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        border: 1px solid #eee;
    }
    .format-item h4 { font-size: 0.95em; margin-bottom: 10px; }
    .format-item ul { padding-left: 16px; }
    .format-item li {
        font-size: 0.85em;
        color: #555;
        margin-bottom: 6px;
        line-height: 1.5;
    }

    /* Insight Grid */
    .insight-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 14px;
    }
    .insight-card {
        background: #fff;
        border-left: 4px solid #1a1a2e;
        border-radius: 0 8px 8px 0;
        padding: 16px 20px;
        font-size: 0.88em;
        color: #444;
        line-height: 1.7;
    }
    .insight-icon {
        display: inline-block;
        width: 22px;
        height: 22px;
        background: #1a1a2e;
        color: #fff;
        text-align: center;
        border-radius: 50%;
        font-size: 0.8em;
        font-weight: 700;
        line-height: 22px;
        margin-bottom: 6px;
    }

    .case-summary {
        background: #1a1a2e;
        color: #fff;
        border-radius: 10px;
        padding: 20px 24px;
        margin-top: 28px;
        text-align: center;
        font-size: 0.95em;
    }
    .case-summary strong { color: #ffd700; }

    /* Works Grid */
    .works-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 16px;
        margin-top: 20px;
    }
    .work-card {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        border: 1px solid #eee;
    }
    .work-card h4 {
        font-size: 0.95em;
        margin: 10px 0 6px;
    }
    .work-card p {
        font-size: 0.83em;
        color: #555;
        line-height: 1.5;
    }
    .work-data {
        margin-top: 10px;
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
        font-size: 0.8em;
        color: #888;
    }

    /* Tool Grid */
    .tool-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 20px;
    }
    .tool-category {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        border: 1px solid #eee;
    }
    .tool-category h3 {
        font-size: 0.95em;
        margin-bottom: 10px;
        padding-bottom: 6px;
        border-bottom: 2px solid #e8edf5;
    }
    .tool-category .skills { gap: 6px; }
    .tool-category .skill-tag {
        font-size: 0.82em;
        padding: 4px 12px;
    }

    @media (max-width: 700px) {'''

html = html.replace('    @media (max-width: 700px) {', new_css)

# 6. Add mobile responsive for new grids
old_mobile = '''      .platform-grid { grid-template-columns: 1fr; }
      .strategy-grid { grid-template-columns: 1fr; }'''

new_mobile = '''      .platform-grid { grid-template-columns: 1fr; }
      .strategy-grid { grid-template-columns: 1fr; }
      .case-grid-3 { grid-template-columns: 1fr; }
      .format-grid { grid-template-columns: 1fr; }
      .insight-grid { grid-template-columns: 1fr; }
      .works-grid { grid-template-columns: 1fr; }
      .tool-grid { grid-template-columns: 1fr; }'''

html = html.replace(old_mobile, new_mobile)

with open(r'F:\AI大模型学习\找工作\01 简历\winnwu-portfolio\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Done - index.html updated')

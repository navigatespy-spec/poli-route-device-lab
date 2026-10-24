POLI-ROUTE shell-51 + shell-52 統合更新版（検証用）

今回の統合版は、shell-52をベースにshell-51のアイコン画像・PWA設定を同梱したものです。
すでにshell-51を公開していなくても、まとめて更新できます。

含まれる主な改善:
- shell-51: 車寄せ・正面入口の情報を事前登録なしでも調べるためのリンク
- shell-51: アプリ内アイコン位置調整／ホーム画面アイコン更新
- shell-52: 出発・到着の2タップ走行時間記録と次回の参考表示
- 以前の「今日の運転」5ステップ／「ルート保存」4ステップ／駐車場検索も維持

GitHubのサイト版での更新:
1) 更新前にアプリのJSONバックアップを保存（実データはGitHubに上げない）
2) このZIPを解凍する。ZIP自体はGitHubにアップロードしない。
3) GitHubの navigatespy-spec/poli-route-device-lab を開く。
4) Add file → Upload files に以下をアップロード:
   index.html / sw.js / manifest.webmanifest / icons フォルダ内のPNG計6枚
   （READMEは任意で、アップロード不要）
5) Commit changes を押す。
6) 公開したiPhoneのSafariで最新版を確認する。

注: GitHub Pagesは公開サイト。後輩専用施設・ルール・JSONバックアップはアップロード禁止。
注: iPhoneホーム画面のアイコンには古い画像キャッシュが残る場合があります。アプリ削除は保存データを消すおそれがあるため、事前に削除しないでください。
注: iPhone実機でのshell-51/52統合動作は未検証。運転中の操作や後輩の実務利用はまだ行わないでください。

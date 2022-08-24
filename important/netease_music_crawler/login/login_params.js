function make_good(e, t, n) {
        "use strict";
        var r = n(112)
          , o = n(113);
        function i(e, t) {
            var n = r.enc.Utf8.parse(t)
              , t = r.enc.Utf8.parse("0102030405060708")
              , e = r.enc.Utf8.parse(e);
            return r.AES.encrypt(e, n, {
                iv: t,
                mode: r.mode.CBC
            }).toString()
        }
        function c(e, t, n) {
            return o.setMaxDigits(131),
            n = new o.RSAKeyPair(t,"",n),
            o.encryptedString(n, e)
        }
        e.exports = {
            asrsea: function(e, t, n, r) {
                var o = {}
                  , a = function(e) {
                    for (var t, n = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", r = "", o = 0; o < e; o += 1)
                        t = Math.random() * n.length,
                        t = Math.floor(t),
                        r += n.charAt(t);
                    return r
                }(16);
                return o.encText = i(e, r),
                o.encText = i(o.encText, a),
                o.encSecKey = c(a, t, n),
                o
            },
            ecnonasr: function(e, t, n, r) {
                var o = {};
                return o.encText = c(e + r, t, n),
                o
            }
        }
    }
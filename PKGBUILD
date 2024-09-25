pkgname=codeback
pkgrel=1
pkgver=0.1
pkgdesc="efficiency tool for connecting to remote servers and back calling vscode remote session"
url=""
arch=(x86_64)
license=('GPL')
depends=('openssh' 'vscode')
makedepends=()
provides=()
conflicts=()
groups=()

source=('connect' 'codeback' '99-codeback.conf')
sha256sums=('SKIP' 'SKIP' 'SKIP')

package() {
  install -Dm755 $srcdir/connect $pkgdir/usr/bin/connect
  install -Dm755 $srcdir/codeback $pkgdir/usr/bin/codeback
  install -Dm644 $srcdir/99-codeback.conf $pkgdir/etc/ssh/sshd_config.d/99-codeback.conf
}
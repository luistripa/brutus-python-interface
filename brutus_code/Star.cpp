#include "Star.h"

Star::Star() {
  r.assign(3,"0");
  v.assign(3,"0");
  a.assign(3,"0");
  a0.assign(3,"0");
}
Star::Star(mpreal m, std::vector<mpreal> r, std::vector<mpreal> v) {
  this->m = m;
  this->r = r;
  this->v = v;
}




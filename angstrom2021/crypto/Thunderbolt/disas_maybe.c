// enc(inp + flag, list[len(inp)+len(flag)], len(inp)+len(flag));
void enc(long param_1,long param_2,long param_3)
{
  uint uVar1;
  int iVar2;
  long lVar3;
  ulong uVar4;
  uint uVar5;
  long lVar6;
  uint uVar7;
  // f: int[0x100]
  
  if (param_3 != 0) {
    uVar4 = (ulong)s;
    lVar6 = 0;
    lVar3 = 0;
    for(lVar6=0; lVar6<param_3; lVar6++)
      iVar2 = (int)uVar4 + f[lVar3];
      s = f[iVar2 % 0x100];
      uVar4 = SEXT48((int)s);
      swap(f[uVar4], f[lVar3]);
      lVar3 = (lVar3 + 1) % 0x100;
      
      param_2[lVar6] = f[f[f[s]] + 1 % 0x100] ^ param_1[lVar6];
    }
    return;
  }
  return;
}

// fgen(os.urandom(len(inp)+len(flag)), os.urandom(1), len(inp)+len(flag), 0x10);
void fgen(long param_1,long param_2,ulong param_3,ulong param_4)
{
  int iVar1;
  ulong uVar3;
  uint uVar4;
  ulong uVar5;
  ulong uVar6;
  ulong uVar7;
  rand1 = List[len(inp)+len(flag)]
  rand2 = List[1]
  leng1 = len(inp)+len(flag)
  leng2 = 1
  
  // int f[0x100] = [0,1,2,3,...,255]  
  // lVar2 = 0;
  //do {
  //  *(int *)(f + lVar2 * 4) = (int)lVar2;
  //  lVar2 = lVar2 + 1;
  //} while (lVar2 != 0x100);
  uVar3 = (ulong)s;
  for(uVar6=0; uVar6<0x300; uVar6++){
    uVar5 = uVar6 % 0x100;
    iVar1 = rand1[uVar6 % leng1] + (int)uVar3 + f[uVar5];
    s = f[iVar1 % 0x100];
    uVar3 = SEXT48((int)s);
    swap(f[uVar3], f[uVar5]);
  }
  for(uVar6=0; uVar6<0x300; uVar6++){ 
    uVar5 = uVar6 % 0x100;
    iVar1 = rand2[uVar6 % leng2] + (int)uVar3 + f[uVar5];
    s = f[iVar1 % 0x100];
    uVar3 = SEXT48((int)s);
    swap(f[uVar3], f[uVar5]);
  }
  return;
}
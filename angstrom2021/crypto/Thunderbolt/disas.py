inp = "AAA"
flag = "actf{...}"
local_158 = inp + flag # +"\x00"
local_148 = os.urandom(2) # 0x10 bit

sVar2 = len(inp)
#__size = len(flag)
iVar5 = len(inp)+len(flag)
__size = len(inp)+len(flag)

# __ptr_00 : list[len(inp)+len(flag)], os.urandom(len(inp)+len(flag))
# __ptr_01 : list[len(inp)+len(flag)]

fgen(__ptr_00, local_148, len(inp)+len(flag), 0x10);
enc(*local_158, __ptr_01, len(inp)+len(flag));

if 0 < iVar5:
    print(__ptr_01) # hex

# enc(inp + flag, list[len(inp)+len(flag)], len(inp)+len(flag));
void enc(long param_1,long param_2,long param_3)
{
  uint uVar1;
  int iVar2;
  long lVar3;
  ulong uVar4;
  uint uVar5;
  long lVar6;
  uint uVar7;
  
  if (param_3 != 0) {
    uVar4 = (ulong)s;
    lVar6 = 0;
    uVar5 = 0;
    do {
      lVar3 = (long)(int)uVar5;
      iVar2 = (int)uVar4 + *(int *)(f + lVar3 * 4);
      uVar5 = uVar5 + 1 & 0xff;
      uVar7 = (uint)(iVar2 >> 0x1f) >> 0x18;
      s = *(uint *)(f + (long)(int)((iVar2 + uVar7 & 0xff) - uVar7) * 4);
      uVar7 = (uint)(*(int *)(f + (long)*(int *)(f + (long)(int)s * 4) * 4) + 1 >> 0x1f) >> 0x18;
      *(byte *)(param_2 + lVar6) =
           (byte)*(undefined4 *)
                  (f + (long)(int)((*(int *)(f + (long)*(int *)(f + (long)(int)s * 4) * 4) + 1 +
                                    uVar7 & 0xff) - uVar7) * 4) ^ *(byte *)(param_1 + lVar6);
      uVar4 = SEXT48((int)s);
      lVar6 = lVar6 + 1;
      uVar7 = *(uint *)(f + lVar3 * 4);
      uVar1 = *(uint *)(f + uVar4 * 4);
      *(uint *)(f + lVar3 * 4) = uVar7 ^ uVar1;
      uVar7 = uVar7 ^ uVar1 ^ *(uint *)(f + uVar4 * 4);
      *(uint *)(f + uVar4 * 4) = uVar7;
      *(uint *)(f + lVar3 * 4) = *(uint *)(f + lVar3 * 4) ^ uVar7;
    } while (param_3 != lVar6);
    return;
  }
  return;
}

# fgen(os.urandom(len(inp)+len(flag)), os.urandom(1), len(inp)+len(flag), 0x10);
void fgen(long param_1,long param_2,ulong param_3,ulong param_4)
{
  int iVar1;
  long lVar2;
  ulong uVar3;
  uint uVar4;
  ulong uVar5;
  ulong uVar6;
  ulong uVar7;
  
  lVar2 = 0;
  do {
    *(int *)(f + lVar2 * 4) = (int)lVar2;
    lVar2 = lVar2 + 1;
  } while (lVar2 != 0x100);
  uVar3 = (ulong)s;
  uVar6 = 0;
  do {
    uVar7 = uVar6 & 0xff;
    uVar5 = uVar6 + 1;
    iVar1 = (uint)*(byte *)(param_1 + uVar6 % param_3) + (int)uVar3 + *(uint *)(f + uVar7 * 4);
    uVar4 = (uint)(iVar1 >> 0x1f) >> 0x18;
    uVar3 = SEXT48(*(int *)(f + (long)(int)((iVar1 + uVar4 & 0xff) - uVar4) * 4));
    uVar4 = *(uint *)(f + uVar7 * 4) ^ *(uint *)(f + uVar3 * 4);
    *(uint *)(f + uVar7 * 4) = uVar4;
    uVar4 = uVar4 ^ *(uint *)(f + uVar3 * 4);
    *(uint *)(f + uVar3 * 4) = uVar4;
    *(uint *)(f + uVar7 * 4) = *(uint *)(f + uVar7 * 4) ^ uVar4;
    uVar6 = uVar5;
  } while (uVar5 != 0x300);
  uVar6 = 0;
  do {
    uVar5 = uVar6 & 0xff;
    uVar7 = uVar6 + 1;
    iVar1 = (uint)*(byte *)(param_2 + uVar6 % param_4) + (int)uVar3 + *(uint *)(f + uVar5 * 4);
    uVar4 = (uint)(iVar1 >> 0x1f) >> 0x18;
    s = *(uint *)(f + (long)(int)((iVar1 + uVar4 & 0xff) - uVar4) * 4);
    uVar3 = SEXT48((int)s);
    uVar4 = *(uint *)(f + uVar5 * 4) ^ *(uint *)(f + uVar3 * 4);
    *(uint *)(f + uVar5 * 4) = uVar4;
    uVar4 = uVar4 ^ *(uint *)(f + uVar3 * 4);
    *(uint *)(f + uVar3 * 4) = uVar4;
    *(uint *)(f + uVar5 * 4) = *(uint *)(f + uVar5 * 4) ^ uVar4;
    uVar6 = uVar7;
  } while (uVar7 != 0x300);
  return;
}
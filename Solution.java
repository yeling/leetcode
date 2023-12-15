/*
 * Decompiled with CFR 0.152.
 */
import kotlin.Metadata;
import kotlin.collections.ArraysKt;
import kotlin.jvm.internal.Intrinsics;
import org.jetbrains.annotations.NotNull;

@Metadata(mv={1, 1, 9}, bv={1, 0, 2}, k=1, d1={"\u0000\u0014\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u0015\n\u0002\b\u0002\u0018\u00002\u00020\u0001B\u0005\u00a2\u0006\u0002\u0010\u0002J\u0016\u0010\u0003\u001a\u00020\u00042\u0006\u0010\u0005\u001a\u00020\u00042\u0006\u0010\u0006\u001a\u00020\u0004"}, d2={"LSolution;", "", "()V", "answerQueries", "", "nums", "queries"})
public final class Solution {
    /*
     * WARNING - void declaration
     */
    @NotNull
    public final int[] answerQueries(@NotNull int[] nums, @NotNull int[] queries) {
        int i;
        Intrinsics.checkParameterIsNotNull(nums, "nums");
        Intrinsics.checkParameterIsNotNull(queries, "queries");
        int n = nums.length;
        int m = queries.length;
        ArraysKt.sort(nums);
        int[] ans = new int[m];
        int[] pre = new int[n + 1];
        int n2 = 0;
        int n3 = nums.length;
        while (n2 < n3) {
            pre[i + true] = nums[i] + pre[i];
            ++i;
        }
        n3 = queries.length;
        for (i = 0; i < n3; ++i) {
            void j;
            int n4 = 0;
            int n5 = nums.length;
            while (n4 < n5 && pre[j + true] <= queries[i]) {
                ans[i] = j + true;
                ++j;
            }
        }
        return ans;
    }
}

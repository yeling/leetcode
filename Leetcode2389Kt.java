/*
 * Decompiled with CFR 0.152.
 */
import java.util.Arrays;
import java.util.List;
import kotlin.Metadata;
import kotlin.collections.CollectionsKt;
import kotlin.jvm.internal.Intrinsics;
import kotlin.ranges.CharRange;
import org.jetbrains.annotations.NotNull;

@Metadata(mv={1, 1, 9}, bv={1, 0, 2}, k=2, d1={"\u0000\u0012\n\u0000\n\u0002\u0010\u0002\n\u0000\n\u0002\u0010\u0011\n\u0002\u0010\u000e\n\u0000\u001a\u0019\u0010\u0000\u001a\u00020\u00012\f\u0010\u0002\u001a\b\u0012\u0004\u0012\u00020\u00040\u0003\u00a2\u0006\u0002\u0010\u0005"}, d2={"main", "", "args", "", "", "([Ljava/lang/String;)V"})
public final class Leetcode2389Kt {
    public static final void main(@NotNull String[] args) {
        Intrinsics.checkParameterIsNotNull(args, "args");
        String string = "Hello Kotlin";
        System.out.println((Object)string);
        int[] nums = new int[]{4, 5, 2, 1};
        int[] queries = new int[]{3, 10, 21};
        Solution sol = new Solution();
        int[] ret = sol.answerQueries(nums, queries);
        String string2 = "" + Arrays.toString(ret);
        System.out.println((Object)string2);
        char c = 'a';
        List chars = CollectionsKt.toList(new CharRange(c, 'z'));
        System.out.println(chars.take(3));
    }
}

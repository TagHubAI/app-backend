import type { ThemeCommonVars } from '../../_styles/common';
import { Theme } from '../../_mixins';
declare const self: (vars: ThemeCommonVars) => {
    color: string;
    colorEnd: string;
    borderRadius: string;
    heightSmall: string;
    heightMedium: string;
    heightLarge: string;
};
export declare type SkeletonThemeVars = ReturnType<typeof self>;
export declare const skeletonLight: Theme<'Skeleton', SkeletonThemeVars>;
export declare type SkeletonTheme = typeof skeletonLight;
export {};

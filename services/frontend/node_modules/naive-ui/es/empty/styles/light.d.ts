import type { ThemeCommonVars } from '../../_styles/common';
import type { Theme } from '../../_mixins';
export declare const self: (vars: ThemeCommonVars) => {
    fontSizeSmall: string;
    fontSizeMedium: string;
    fontSizeLarge: string;
    fontSizeHuge: string;
    textColor: string;
    iconColor: string;
    extraTextColor: string;
    iconSizeSmall: string;
    iconSizeMedium: string;
    iconSizeLarge: string;
    iconSizeHuge: string;
};
export declare type EmptyThemeVars = ReturnType<typeof self>;
declare const emptyLight: Theme<'Empty', EmptyThemeVars>;
export default emptyLight;
export declare type EmptyTheme = typeof emptyLight;

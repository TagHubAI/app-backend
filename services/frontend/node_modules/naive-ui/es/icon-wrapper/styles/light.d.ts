import type { ThemeCommonVars } from '../../_styles/common';
import type { Theme } from '../../_mixins';
export declare const self: (vars: ThemeCommonVars) => {
    color: string;
    iconColor: string;
};
export declare type IconWrapperThemeVars = ReturnType<typeof self>;
declare const iconWrapperLight: Theme<'IconWrapper', IconWrapperThemeVars>;
export default iconWrapperLight;
export declare type IconWrapperTheme = typeof iconWrapperLight;

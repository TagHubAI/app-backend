import { commonLight } from '../../_styles/common';
export const self = (vars) => {
    const { fontWeight, textColor1, textColor2, dividerColor, fontSize } = vars;
    return {
        titleFontSize: fontSize,
        titleFontWeight: fontWeight,
        dividerColor: dividerColor,
        titleTextColor: textColor1,
        fontSize,
        textColor: textColor2,
        arrowColor: textColor2
    };
};
const collapseLight = {
    name: 'Collapse',
    common: commonLight,
    self
};
export default collapseLight;

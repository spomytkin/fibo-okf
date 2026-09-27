---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: 'This ontology defines currency and monetary amount related concepts for use in defining other FIBO ontology elements.
      There are two distinct kinds of concepts that correspond to money and amounts: a concrete, actual amount of money, and
      the monetary measure of something denominated in some currency. These are dimensionally the same but whereas ''money
      amount'' is defined as an amount of money, ''monetary amount'' is an abstract monetary measure.


      The definition of currency provided herein is compliant with the definitions given in ISO 4217. ISO 4217 provides universally
      applicable coded representations of names of currencies and funds, used internationally for financial transaction support.
      The ontology has been partitioned into 2 parts: (1) the essential concept system describing the standard (this module),
      and (2) ISO4217-1-CurrencyCodes, which contains all of the individuals specified in ISO 4217.'
  - predicate: http://purl.org/dc/terms/license
    value: "2013-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2013-2025 Object Management Group, Inc.\n\t\t\n\
      Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation\
      \ files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use,\
      \ copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to\
      \ whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this\
      \ permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED\
      \ 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\
      \ FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE\
      \ FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT\
      \ OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\tSee https://opensource.org/licenses/MIT."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Currency Amount Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The FIBO FND 1.0 (https://spec.edmcouncil.org/fibo/ontology/FND/20141101/Accounting/CurrencyAmount.rdf) version
      of this ontology was modified per the additions introduced in the FIBO FBC RFC and related issue resolutions identified
      in the FIBO FND 1.1 RTF report and https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.1/, including adding
      support for ISO 4217 currency codes.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The FIBO FND 1.1 (https://spec.edmcouncil.org/fibo/ontology/FND/20160201/Accounting/CurrencyAmount.rdf) version
      of this ontology was modified per FIBO 2.0 RFC, including the addition of a new hasMonetaryAmount property as a superproperty
      of others required by various FIBO domain teams and integration with LCC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20000601/Accounting/CurrencyAmount/ version of this ontology
      was modified to replace a redundant concept, calculation formula with formula.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Accounting/CurrencyAmount.rdf version of this ontology
      was modified to include several classes to support automated inclusion of all ISO 4217 codes published as of 2018-06-04,
      and to revise definitions per the eighth edition of the specification.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20181101/Accounting/CurrencyAmount/ version of this ontology
      was modified to use the generic statistical measures and measurements now in FND.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190501/Accounting/CurrencyAmount/ version of this ontology
      was modified to eliminate deprecated elements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190901/Accounting/CurrencyAmount/ version of this ontology
      was modified to improve definitions for notional amount and currency identifier.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20191201/Accounting/CurrencyAmount/ version of this ontology
      was modified to correct the explanatory note on currency identifier.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20191201/Accounting/CurrencyAmount/ version of this ontology
      was modified to eliminate duplication with concepts in LCC, dependencies on a couple of ontologies that were unnecessary,
      eliminate references to external dictionary sites that no longer resolve, clean up ambiguity in definitions, eliminate
      a redundant property, and add unit price.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20210201/Accounting/CurrencyAmount/ version of this ontology
      was modified to loosen a restriction on currency to allow for more than one numeric currency code, which was necessitated
      by the October 2021 update to the ISO currency code definitions.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220101/Accounting/CurrencyAmount/ version of this ontology
      was modified to move the definition of precious metal and the corresponding identifier to this ontology from Products
      and Services to simplify imports in cases where the broader definitions for commodities are not required and deprecated
      isTenderIn, given that we have used the property isUsedBy for this purpose in the currency codes themselves.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220201/Accounting/CurrencyAmount/ version of this ontology
      was modified to add a restriction to indicate the currency on percentage monetary amount, make currency a subclass of
      unit of measure, and deprecate the notion of monetary measure, which is more about monetary policy and was incorrectly
      used in a few places, and is out of scope for our current set of use cases.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220301/Accounting/CurrencyAmount/ version of this ontology
      was modified to eliminate hygiene errors with respect to text formatting.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/Accounting/CurrencyAmount.rdf version of this ontology
      was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Accounting/CurrencyAmount.rdf version of this ontology
      was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC)
      and to eliminate redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Accounting/CurrencyAmount.rdf version of the ontology
      was modified to eliminate deprecations that are more than 6 months old.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20231101/Accounting/CurrencyAmount.rdf version of this ontology
      was modified to tease out the distinction between the nominal and notional amount, which were confused (DER-127) and
      to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20231201/Accounting/CurrencyAmount.rdf version of the ontology
      was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2
      (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20250301/Accounting/CurrencyAmount.rdf version of the ontology
      was modified to replace hasConstituent with hasMember for better semantic consistency (FND-396).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20250701/Accounting/CurrencyAmount.rdf version of the ontology
      was modified to replace references to the now deprecated hasTag property in Relations with its equivalent in OMG Commons
      (FND-412).
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: (1) The present version of the ontology covers the English sections of the ISO 4217 standard only, and (2) UTF-8
      character encodings are employed in names in the currency codes ontology to support the broadest number of tools.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/directSource
    value: ISO 4217 Codes for the representation of currencies and funds, Eighth edition, 2015-08-01
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/directSource
    value: ISO 4217 Codes for the representation of currencies and funds, Seventh edition, 2008-07-15
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20260701/Accounting/CurrencyAmount/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/ContextualDesignators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Designators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Documents/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Identifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Locations/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/TextDatatype/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/
sources:
- id: fibo-source-4355744519
  resource: references/fibo/FND/Accounting/CurrencyAmount.rdf
  sha256: 4355744519e448cbeeedd0e9601a43470dc1329a7cab73d807e7b99048db0032
  title: FIBO source FND/Accounting/CurrencyAmount.rdf
title: Currency Amount Ontology
type: Ontology Definition
---

# Currency Amount Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/>

## Relationships

- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [CodesAndCodeSets](<https://www.omg.org/spec/Commons/CodesAndCodeSets/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [ContextualDesignators](<https://www.omg.org/spec/Commons/ContextualDesignators/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [Documents](<https://www.omg.org/spec/Commons/Documents/>)
- **Related to**: [Identifiers](<https://www.omg.org/spec/Commons/Identifiers/>)
- **Related to**: [Locations](<https://www.omg.org/spec/Commons/Locations/>)
- **Related to**: [QuantitiesAndUnits](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/>)
- **Related to**: [TextDatatype](<https://www.omg.org/spec/Commons/TextDatatype/>)
- **Related to**: [CurrencyAmount](<https://spec.edmcouncil.org/fibo/ontology/FND/20260701/Accounting/CurrencyAmount/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines currency and monetary amount related concepts for use in defining other FIBO ontology elements. There are two distinct kinds of concepts that correspond to money and amounts: a concrete, actual amount of money, and the monetary measure of something denominated in some currency. These are dimensionally the same but whereas 'money amount' is defined as an amount of money, 'monetary amount' is an abstract monetary measure.  The definition of currency provided herein is compliant with the definitions given in ISO 4217. ISO 4217 provides universally applicable coded representations of names of currencies and funds, used internationally for financial transaction support. The ontology has been partitioned into 2 parts: (1) the essential concept system describing the standard (this module), and (2) ISO4217-1-CurrencyCodes, which contains all of the individuals specified in ISO 4217.
- **license**: 2013-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2013-2025 Object Management Group, Inc. 		 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Currency Amount Ontology
- **changeNote**: The FIBO FND 1.0 (https://spec.edmcouncil.org/fibo/ontology/FND/20141101/Accounting/CurrencyAmount.rdf) version of this ontology was modified per the additions introduced in the FIBO FBC RFC and related issue resolutions identified in the FIBO FND 1.1 RTF report and https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.1/, including adding support for ISO 4217 currency codes.
- **changeNote**: The FIBO FND 1.1 (https://spec.edmcouncil.org/fibo/ontology/FND/20160201/Accounting/CurrencyAmount.rdf) version of this ontology was modified per FIBO 2.0 RFC, including the addition of a new hasMonetaryAmount property as a superproperty of others required by various FIBO domain teams and integration with LCC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20000601/Accounting/CurrencyAmount/ version of this ontology was modified to replace a redundant concept, calculation formula with formula.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Accounting/CurrencyAmount.rdf version of this ontology was modified to include several classes to support automated inclusion of all ISO 4217 codes published as of 2018-06-04, and to revise definitions per the eighth edition of the specification.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20181101/Accounting/CurrencyAmount/ version of this ontology was modified to use the generic statistical measures and measurements now in FND.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190501/Accounting/CurrencyAmount/ version of this ontology was modified to eliminate deprecated elements.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190901/Accounting/CurrencyAmount/ version of this ontology was modified to improve definitions for notional amount and currency identifier.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20191201/Accounting/CurrencyAmount/ version of this ontology was modified to correct the explanatory note on currency identifier.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20191201/Accounting/CurrencyAmount/ version of this ontology was modified to eliminate duplication with concepts in LCC, dependencies on a couple of ontologies that were unnecessary, eliminate references to external dictionary sites that no longer resolve, clean up ambiguity in definitions, eliminate a redundant property, and add unit price.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20210201/Accounting/CurrencyAmount/ version of this ontology was modified to loosen a restriction on currency to allow for more than one numeric currency code, which was necessitated by the October 2021 update to the ISO currency code definitions.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220101/Accounting/CurrencyAmount/ version of this ontology was modified to move the definition of precious metal and the corresponding identifier to this ontology from Products and Services to simplify imports in cases where the broader definitions for commodities are not required and deprecated isTenderIn, given that we have used the property isUsedBy for this purpose in the currency codes themselves.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220201/Accounting/CurrencyAmount/ version of this ontology was modified to add a restriction to indicate the currency on percentage monetary amount, make currency a subclass of unit of measure, and deprecate the notion of monetary measure, which is more about monetary policy and was incorrectly used in a few places, and is out of scope for our current set of use cases.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220301/Accounting/CurrencyAmount/ version of this ontology was modified to eliminate hygiene errors with respect to text formatting.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220701/Accounting/CurrencyAmount.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Accounting/CurrencyAmount.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC) and to eliminate redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230301/Accounting/CurrencyAmount.rdf version of the ontology was modified to eliminate deprecations that are more than 6 months old.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20231101/Accounting/CurrencyAmount.rdf version of this ontology was modified to tease out the distinction between the nominal and notional amount, which were confused (DER-127) and to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20231201/Accounting/CurrencyAmount.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20250301/Accounting/CurrencyAmount.rdf version of the ontology was modified to replace hasConstituent with hasMember for better semantic consistency (FND-396).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20250701/Accounting/CurrencyAmount.rdf version of the ontology was modified to replace references to the now deprecated hasTag property in Relations with its equivalent in OMG Commons (FND-412).
- **editorialNote**: (1) The present version of the ontology covers the English sections of the ISO 4217 standard only, and (2) UTF-8 character encodings are employed in names in the currency codes ontology to support the broadest number of tools.
- **copyright**: Copyright (c) 2013-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.
- **directSource**: ISO 4217 Codes for the representation of currencies and funds, Eighth edition, 2015-08-01
- **directSource**: ISO 4217 Codes for the representation of currencies and funds, Seventh edition, 2008-07-15

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

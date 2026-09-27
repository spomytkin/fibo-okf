---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology extends the primary financial services entities ontology in FBC with additional kinds of entities
      that that provide services in Europe, across national boundaries, such as European market data providers, organizations
      that provide exchanges in multiple countries, organizations that support the European Union, and so forth.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2017-2025 EDM Council, Inc.\nCopyright (c) 2017-2025 Object Management Group, Inc.\n\nPermission\
      \ is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files\
      \ (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy,\
      \ modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom\
      \ the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission\
      \ notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED 'AS IS',\
      \ WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\
      \ FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE\
      \ FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT\
      \ OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\tSee https://opensource.org/licenses/MIT."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: European Financial Services Entities Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180801/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities.rdf
      version of this ontology was added via the FIBO 2.0 RFC.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180801/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities.rdf
      version of this ontology was revised to adjust the name of the CreditInstitutionOrInvestmentFirm classification to eliminate
      the 'or' in the name to address hygiene issues.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210801/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities.rdf
      version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than
      the OMG's Specification Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230101/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities.rdf
      version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology
      Library (Commons) v1.2 (FND-389).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2017-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2017-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/20250301/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Organizations/
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/
sources:
- id: fibo-source-760f05a832
  resource: references/fibo/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities.rdf
  sha256: 760f05a8322c75aaef31b7b35eefe1470b4bd58ea40a9be94100e8fe641fce43
  title: FIBO source FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities.rdf
title: European Financial Services Entities Ontology
type: Ontology Definition
---

# European Financial Services Entities Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/>

## Relationships

- **Related to**: [FinancialServicesEntities](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities.md)
- **Related to**: [FinancialProductsAndServices](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Organizations](<https://www.omg.org/spec/Commons/Organizations/>)
- **Related to**: [EUFinancialServicesEntities](<https://spec.edmcouncil.org/fibo/ontology/FBC/20250301/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology extends the primary financial services entities ontology in FBC with additional kinds of entities that that provide services in Europe, across national boundaries, such as European market data providers, organizations that provide exchanges in multiple countries, organizations that support the European Union, and so forth.
- **license**: Copyright (c) 2017-2025 EDM Council, Inc. Copyright (c) 2017-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: European Financial Services Entities Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180801/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities.rdf version of this ontology was added via the FIBO 2.0 RFC.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20180801/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities.rdf version of this ontology was revised to adjust the name of the CreditInstitutionOrInvestmentFirm classification to eliminate the 'or' in the name to address hygiene issues.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20210801/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities.rdf version of the ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FBC/20230101/FunctionalEntities/EuropeanEntities/EUFinancialServicesEntities.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **copyright**: Copyright (c) 2017-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2017-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

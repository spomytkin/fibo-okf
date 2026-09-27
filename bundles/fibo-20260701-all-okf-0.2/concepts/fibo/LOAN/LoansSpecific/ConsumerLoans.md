---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: The consumer loans ontology defines concepts specific to loans that are offered only to consumers rather than to
      organization, primarily for personal, family, or household purposes.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2015-2025 EDM Council, Inc.\nCopyright (c) 2015-2025 Object Management Group, Inc.\n\t\t\nPermission\
      \ is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files\
      \ (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy,\
      \ modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom\
      \ the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission\
      \ notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED 'AS IS',\
      \ WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\
      \ FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE\
      \ FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT\
      \ OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\tSee https://opensource.org/licenses/MIT."
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Consumer Loans Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/LOAN/20230901/LoansSpecific/ConsumerLoans.rdf version of the ontology
      was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380) and
      to integrate the concept that a HELOC is a loan secured by real estate (LOAN-169).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/LOAN/20241101/LoansSpecific/ConsumerLoans.rdf version of the ontology
      was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2
      (FND-389).
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2015-2025 EDM Council, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2015-2025 Object Management Group, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/BE/LegalEntities/LegalPersons.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LegalPersons/
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/20250301/LoansSpecific/ConsumerLoans/
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/
  - concept: /concepts/fibo/LOAN/RealEstateLoans/Mortgages.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/RolesAndCompositions/
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/ConsumerLoans/
sources:
- id: fibo-source-7c7642cd54
  resource: references/fibo/LOAN/LoansSpecific/ConsumerLoans.rdf
  sha256: 7c7642cd546c2c1de619d2ea9b384b314886dedf7c8601dab9a46870d0e591d7
  title: FIBO source LOAN/LoansSpecific/ConsumerLoans.rdf
title: Consumer Loans Ontology
type: Ontology Definition
---

# Consumer Loans Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/ConsumerLoans/>

## Relationships

- **Related to**: [LegalPersons](/concepts/fibo/BE/LegalEntities/LegalPersons.md)
- **Related to**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Related to**: [ProductsAndServices](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [Loans](/concepts/fibo/LOAN/LoansGeneral/Loans.md)
- **Related to**: [Mortgages](/concepts/fibo/LOAN/RealEstateLoans/Mortgages.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [RolesAndCompositions](<https://www.omg.org/spec/Commons/RolesAndCompositions/>)
- **Related to**: [ConsumerLoans](<https://spec.edmcouncil.org/fibo/ontology/LOAN/20250301/LoansSpecific/ConsumerLoans/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: The consumer loans ontology defines concepts specific to loans that are offered only to consumers rather than to organization, primarily for personal, family, or household purposes.
- **license**: Copyright (c) 2015-2025 EDM Council, Inc. Copyright (c) 2015-2025 Object Management Group, Inc. 		 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label** (en): Consumer Loans Ontology
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/LOAN/20230901/LoansSpecific/ConsumerLoans.rdf version of the ontology was modified to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380) and to integrate the concept that a HELOC is a loan secured by real estate (LOAN-169).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/LOAN/20241101/LoansSpecific/ConsumerLoans.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **copyright**: Copyright (c) 2015-2025 EDM Council, Inc.
- **copyright**: Copyright (c) 2015-2025 Object Management Group, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

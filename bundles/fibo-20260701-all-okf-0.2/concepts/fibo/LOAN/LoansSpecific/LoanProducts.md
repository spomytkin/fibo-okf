---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology describes loan and mortgage loan products. A product as defined here is something marketed and offered
      for sale, in this case a loan, such that when a customer takes on the product, they become signatories to a corresponding
      loan contract. A loan product in this sense is a contractual, off-the-shelf product with terms corresponding to those
      in the actual contract when it is signed.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://purl.org/dc/terms/license
    value: https://opensource.org/licenses/MIT
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Loan Products Ontology
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2016-2024 EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/
  - concept: /concepts/fibo/FND/Agreements/Contracts.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/
  - concept: /concepts/fibo/FND/Arrangements/ClassificationSchemes.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/
  - concept: /concepts/fibo/FND/GoalsAndObjectives/Objectives.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/GoalsAndObjectives/Objectives/
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/
  - concept: /concepts/fibo/FND/Relations/Relations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Provisional.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Provisional
  - concept: /concepts/fibo/LOAN/LoansGeneral/Loans.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/
  - concept: /concepts/fibo/LOAN/LoansGeneral/LoansRegulatory.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/
  - concept: /concepts/fibo/LOAN/LoansSpecific/LoanProducts.md
    predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/
  - concept: /concepts/fibo/LOAN/RealEstateLoans/MortgageOrigination.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/
  - concept: /concepts/fibo/LOAN/RealEstateLoans/Mortgages.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Classifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/ContextualDesignators/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Documents/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/
sources:
- id: fibo-source-1b62e30b1c
  resource: references/fibo/LOAN/LoansSpecific/LoanProducts.rdf
  sha256: 1b62e30b1c3693cc85e718679f9b231242d1342cdfc54a4c99663db4f26a8644
  title: FIBO source LOAN/LoansSpecific/LoanProducts.rdf
title: Loan Products Ontology
type: Ontology Definition
---

# Loan Products Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansSpecific/LoanProducts/>

## Relationships

- **Related to**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **Related to**: [FinancialProductsAndServices](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.md)
- **Related to**: [CurrencyAmount](/concepts/fibo/FND/Accounting/CurrencyAmount.md)
- **Related to**: [Contracts](/concepts/fibo/FND/Agreements/Contracts.md)
- **Related to**: [ClassificationSchemes](/concepts/fibo/FND/Arrangements/ClassificationSchemes.md)
- **Related to**: [Objectives](/concepts/fibo/FND/GoalsAndObjectives/Objectives.md)
- **Related to**: [ProductsAndServices](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [Loans](/concepts/fibo/LOAN/LoansGeneral/Loans.md)
- **Related to**: [LoansRegulatory](/concepts/fibo/LOAN/LoansGeneral/LoansRegulatory.md)
- **Related to**: [MortgageOrigination](/concepts/fibo/LOAN/RealEstateLoans/MortgageOrigination.md)
- **Related to**: [Mortgages](/concepts/fibo/LOAN/RealEstateLoans/Mortgages.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Classifiers](<https://www.omg.org/spec/Commons/Classifiers/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [ContextualDesignators](<https://www.omg.org/spec/Commons/ContextualDesignators/>)
- **Related to**: [Documents](<https://www.omg.org/spec/Commons/Documents/>)
- **Related to**: [QuantitiesAndUnits](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/>)
- **Related to**: [LoanProducts](/concepts/fibo/LOAN/LoansSpecific/LoanProducts.md)
- **Related to**: [Provisional](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Provisional.md)

## Annotations

- **abstract**: This ontology describes loan and mortgage loan products. A product as defined here is something marketed and offered for sale, in this case a loan, such that when a customer takes on the product, they become signatories to a corresponding loan contract. A loan product in this sense is a contractual, off-the-shelf product with terms corresponding to those in the actual contract when it is signed.
- **license**: https://opensource.org/licenses/MIT
- **label** (en): Loan Products Ontology
- **copyright**: Copyright (c) 2016-2024 EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

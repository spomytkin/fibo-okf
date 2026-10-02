---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: mortgage indemnity guarantee
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: insurance-backed guarantee that protects lenders if the mortgage repayments cease for some reason, perhaps due
      to death or a homeowner being made redundant at work
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'See notes from SME Review and in MIG Provider. Applies to securitized pool, insures the lender. Additional note
      (IBM): there is a further application of this. When a lender takes a loan which is a where the value of the loan is
      greater than 80% of the value of the property, at that point it is required for the lender to also get a private mortgage
      insurance, so they are paying separately for the mortgage insurance so that if the borrower defaults above 80% then
      the mortgage insurance pays the loss. In the Loan Party Insurer (new "Party" type) you have Loan Party Insured Ratio
      (e.g. the 80% in the example above). These are different situations but the same principle. So this needs to be modeled
      for both. 30 June: Is this Lender or Borrower? since you have one lender and one borrower in a single loan, but multiple
      lenders in the case of packaging this up for a security - there are then multiple lenders and multiple borrowers. A
      similar kind of insurance exists in the one lender one borrower scenario i.e. the mortgage loan itself. There are two
      concepts here. the MIG thing was for bundling these. the MIG might apply across multiple contracts, but still be a fact
      about "the" contract? The notes about 80% above (IBM) are about the individual loan. ACTION: Tidy this up.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/MortgageIndemnityGuarantor
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/isGuaranteedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/MortgageIndemnityInsurancePolicy
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isExemplifiedBy
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Guaranty/InsuranceBackedGuaranty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/InsuranceBackedGuaranty
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/MortgageIndemnityGuarantee
sources:
- id: fibo-source-939ceaa7d7
  resource: references/fibo/LOAN/RealEstateLoans/MortgageOrigination.rdf
  sha256: 939ceaa7d7758108e99a4653c0d982fdf5cb9bce32f07927542f3b01508e593a
  title: FIBO source LOAN/RealEstateLoans/MortgageOrigination.rdf
title: mortgage indemnity guarantee
type: Ontology Class
---

# mortgage indemnity guarantee

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/MortgageOrigination/MortgageIndemnityGuarantee>

## Definition

insurance-backed guarantee that protects lenders if the mortgage repayments cease for some reason, perhaps due to death or a homeowner being made redundant at work

## Relationships

- **Subclass of**: [InsuranceBackedGuaranty](/concepts/fibo/FBC/DebtAndEquities/Guaranty/InsuranceBackedGuaranty.md)

## Constraints

- **[isGuaranteedBy](/concepts/fibo/FBC/DebtAndEquities/Guaranty/isGuaranteedBy.md)**: some values from of type [MortgageIndemnityGuarantor](/concepts/fibo/LOAN/RealEstateLoans/MortgageOrigination/MortgageIndemnityGuarantor.md)
- **[isExemplifiedBy](/concepts/fibo/FND/Relations/Relations/isExemplifiedBy.md)**: some values from of type [MortgageIndemnityInsurancePolicy](/concepts/fibo/LOAN/RealEstateLoans/MortgageOrigination/MortgageIndemnityInsurancePolicy.md)

## Annotations

- **label** (en): mortgage indemnity guarantee
- **definition** (en): insurance-backed guarantee that protects lenders if the mortgage repayments cease for some reason, perhaps due to death or a homeowner being made redundant at work
- **editorialNote** (en): See notes from SME Review and in MIG Provider. Applies to securitized pool, insures the lender. Additional note (IBM): there is a further application of this. When a lender takes a loan which is a where the value of the loan is greater than 80% of the value of the property, at that point it is required for the lender to also get a private mortgage insurance, so they are paying separately for the mortgage insurance so that if the borrower defaults above 80% then the mortgage insurance pays the loss. In the Loan Party Insurer (new "Party" type) you have Loan Party Insured Ratio (e.g. the 80% in the example above). These are different situations but the same principle. So this needs to be modeled for both. 30 June: Is this Lender or Borrower? since you have one lender and one borrower in a single loan, but multiple lenders in the case of packaging this up for a security - there are then multiple lenders and multiple borrowers. A similar kind of insurance exists in the one lender one borrower scenario i.e. the mortgage loan itself. There are two concepts here. the MIG thing was for bundling these. the MIG might apply across multiple contracts, but still be a fact about "the" contract? The notes about 80% above (IBM) are about the individual loan. ACTION: Tidy this up.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.

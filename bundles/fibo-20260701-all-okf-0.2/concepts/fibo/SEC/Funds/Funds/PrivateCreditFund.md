---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: private credit fund
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: investment vehicle that provides loans or other forms of credit to companies, typically outside of the traditional
      banking system
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'These funds are managed by asset managers, private equity firms or specialized lenders (both nonprofit and for-profit)
      and cater to institutional investors, high-net-worth individuals, family offices, and, in some cases, retail investors.
      The kinds of loans they provide include senior secured loans, mezzanine debt, unitranche loans, and special situations
      financing through direct lending to companies. These funds are typically illiquid, with long investment horizons (5–10
      years). They generally provide higher returns than traditional fixed-income instruments, but with greater risk due to
      borrower default potential. Nonprofit funds may provide lower returns because of the mission to provide affordable funding
      to disadvantaged borrowers. Key features of private credit funds include:

      - Loans are held on the fund''s balance sheet

      - Returns come primarily from interest income and potential capital appreciation

      - Often involve direct negotiations and customized loan terms.'
  disjoint_with:
  - concept: /concepts/fibo/SEC/Funds/Funds/PrivateEquityFund.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/PrivateEquityFund
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/PrivateFund.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/PrivateFund
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/PrivateCreditFund
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: private credit fund
type: Ontology Class
---

# private credit fund

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/PrivateCreditFund>

## Definition

investment vehicle that provides loans or other forms of credit to companies, typically outside of the traditional banking system

## Relationships

- **Subclass of**: [PrivateFund](/concepts/fibo/SEC/Securities/Pools/PrivateFund.md)

## Constraints

- **Disjoint with**: [PrivateEquityFund](/concepts/fibo/SEC/Funds/Funds/PrivateEquityFund.md)

## Annotations

- **label** (en): private credit fund
- **definition** (en): investment vehicle that provides loans or other forms of credit to companies, typically outside of the traditional banking system
- **explanatoryNote** (en): These funds are managed by asset managers, private equity firms or specialized lenders (both nonprofit and for-profit) and cater to institutional investors, high-net-worth individuals, family offices, and, in some cases, retail investors. The kinds of loans they provide include senior secured loans, mezzanine debt, unitranche loans, and special situations financing through direct lending to companies. These funds are typically illiquid, with long investment horizons (5–10 years). They generally provide higher returns than traditional fixed-income instruments, but with greater risk due to borrower default potential. Nonprofit funds may provide lower returns because of the mission to provide affordable funding to disadvantaged borrowers. Key features of private credit funds include: - Loans are held on the fund's balance sheet - Returns come primarily from interest income and potential capital appreciation - Often involve direct negotiations and customized loan terms.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
